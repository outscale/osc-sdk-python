import sys

sys.path.append("..")
from osc_sdk_python import Problem, ProblemDecoder
import json


def test_deserialize_problem1():
    obj = json.loads(
        """
{
 "type": "https://example.com/probs/out-of-credit",
 "title": "You do not have enough credit.",
 "detail": "Your current balance is 30, but that costs 50.",
 "instance": "/account/12345/msgs/abc",
 "balance": 30,
 "accounts": ["/account/12345",
              "/account/67890"]
}
               """,
        cls=ProblemDecoder,
    )
    assert isinstance(obj, Problem)
    assert obj.extras.get("balance") == 30


def test_deserialize_problem2():
    obj = json.loads(
        """
{
 "type": "https://example.net/validation-error",
 "title": "Your request is not valid.",
 "errors": [
             {
               "detail": "must be a positive integer",
               "pointer": "#/age"
             },
             {
               "detail": "must be 'green', 'red' or 'blue'",
               "pointer": "#/profile/color"
             }
          ]
}
               """,
        cls=ProblemDecoder,
    )
    assert isinstance(obj, Problem)
    assert obj.type == "https://example.net/validation-error"
