import pytest,allure

@allure.severity(allure.severity_level.BLOCKER)
class TestBlocker():
    def test_blocker(self):
        print("test_blocker")

@allure.severity(allure.severity_level.CRITICAL)
class TestCritical():
    def test_critical(self):
        print("test_critical")

@allure.severity(allure.severity_level.NORMAL)
class TestNormal():
    def test_normal(self):
        print("test_normal")

@allure.severity(allure.severity_level.MINOR)
class TestMinor():
    def test_minor(self):
        print("test_minor")

@allure.severity(allure.severity_level.TRIVIAL)
class TestTrivial():
    def test_trivial(self):
        print("test_trivial")