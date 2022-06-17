import os

from main import init_context, handler
from fixtures.fixtures_nuclio import Context, Event


def test_main():
    """
    Runs main nuclio function with a fake nuclio context
    """
    context = Context()
    init_context(context)

    event = Event(image_path=os.path.join(os.getcwd(), "./fixtures/milk.jpg"), threshold=0.5)
    response = handler(context, event)
    assert (
        response.body
        == '[{"confidence": 1.0, "label": "milk_bottle", "points": [240, 190, 356, 494], "type": "rectangle"}]'
    )
