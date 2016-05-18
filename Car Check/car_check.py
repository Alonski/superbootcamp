from collections import defaultdict


# def types():
#     return {
#         'passed': False
#     }

class Report:

    def __init__(self, car_name):
        self.car_name = car_name
        self.tests = []

    def add_check(self, test_type, test_passed):
        self.tests.append((test_type, test_passed))

    def passed(self):
        return all(test[1] for test in self.tests)
        # for test_type, test_passed in self.tests:
        #     if not bool(test_passed):
        #         return False
        # return True

    def render(self):
        output_test = ''
        for test_type, test_passed in self.tests:
            output_test += "* {}: {}\n".format(test_type, "OK" if test_passed else "Failed")

        RESULT_TOTAL = """

Results for car #{}
{}{}PASSED

        """.strip().format(self.car_name, output_test, "" if self.passed() else "NOT ")
        return RESULT_TOTAL

    def print_tests(self):
        for test_type, test_passed in self.tests:
            print(test_type, test_passed)
    pass
