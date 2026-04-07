import pytest
import base64
from pathlib import Path
from datetime import datetime
from slugify import slugify
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from pytest_metadata.plugin import metadata_key

# 1) ADD's CLI OPTIONS
def pytest_addoption(parser):
    # We keep 'default' as None to see if user provided anything
    parser.addoption("--browser", action="store")
    parser.addoption("--headless", action="store_true")


# 2) FETCH CLI VALUE USING FIXTURE
@pytest.fixture(scope="class")
def setup(request):
    # Get values from CLI. If browser is not provided, default to 'chrome'
    browser_choice = request.config.getoption("--browser") or "chrome"
    browser = browser_choice.lower()
    headless = request.config.getoption("--headless")

    print(f"-->>>>>---- Launching {browser.upper()} Browser  ---")
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_experimental_option("detach", True)
        driver: WebDriver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver: WebDriver = webdriver.Firefox(options=options)

    elif browser == "edge":
        options = webdriver.EdgeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_experimental_option("detach", True)
        driver: WebDriver = webdriver.Edge(options=options)
    else:
        raise pytest.UsageError(print("Error:", browser," is not a supported browser. Use text as chrome, firefox, or edge."))

    driver.maximize_window()
    driver.implicitly_wait(10)

    #   --TEAR DOWN with Yield
    yield driver
    print("----->>> ",browser.upper(), "Browser execution completed.")
    driver.quit()

# ------->>>>>>CONFIGURE REPORTS + METADATA WITH PYTEST HOOK.<<<<<<----------------
@pytest.hookimpl
def pytest_configure(config):

    config.stash[metadata_key]["Project Name"] = "Practice WebSite"
    config.stash[metadata_key]["Module Name"] = "Test Module"
    config.stash[metadata_key]["Tester Name"] = "Sk Khaja Mohiddin"

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    base_dir = Path("reports") / timestamp
    html_dir = base_dir / "HtmlReports"
    screenshot_dir = base_dir / "screenshots"

    html_dir.mkdir(parents=True, exist_ok=True)
    screenshot_dir.mkdir(parents=True, exist_ok=True)

    (html_dir / ".gitkeep").touch()
    (screenshot_dir / ".gitkeep").touch()

    config.option.htmlpath = str(html_dir / "report.html")
    config._report_base_dir = base_dir

# REMOVE UNWANTED METADATA
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

    #  --------->>>>>>> SCREENSHOT ON FAILURE <<<<<<<<<--------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call":

        driver = item.funcargs.get("setup", None)

        if report.failed and driver:

            base_dir = getattr(item.config, "_report_base_dir", Path("reports"))
            screenshot_dir = base_dir / "screenshots"

            test_name = slugify(item.nodeid)
            timestamp = datetime.now().strftime("%H-%M-%S")

            file_name = f"{test_name}_{timestamp}.png"
            img_path = screenshot_dir / file_name

            # Save screenshot
            driver.save_screenshot(str(img_path))

            # Attach to HTML report
            pytest_html = item.config.pluginmanager.getplugin("html")

            if pytest_html:
                with open(img_path, "rb") as f:
                    encoded = base64.b64encode(f.read()).decode()

                extra = getattr(report, "extras", [])
                extra.append(
                    pytest_html.extras.image(encoded, mime_type="image/png")
                )
                report.extras = extra