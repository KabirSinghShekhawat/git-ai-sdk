import json


"""
<code>
{
  "type": ["all", "public", "private"],
  "sort": ["created", "updated", "pushed_at"],
  "direction": ["asc", "desc"],
  "per_page": [1-100]
}
</code>
"""


def get_valid_params(resource_name: str):
    prompt = f"Return a dict containg the valid parameters for {resource_name} API."
    prompt += "Wrap all code in <code></code> blocks."



class Validator:
    pass
