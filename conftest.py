import pytest


@pytest.fixture()
def browser_context(browser):
    context = browser.new_context(record_video_dir="artifacts/videos/")
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context

    context.tracing.stop(path="artifacts/traces/trace.zip")
    context.close()
