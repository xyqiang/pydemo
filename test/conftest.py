import pytest

@pytest.fixture()
def login():
    print("登录")

# def pytest_collection_modifyitems(session, config, items:list):
#     # print(items)
#     # print(type(items))
#     for item in items:
#         if "add" in item.nodeid:
#             item.add_marker(pytest.mark.add)
#         elif "div" in item.nodeid:
#             item.add_marker(pytest.mark.div)