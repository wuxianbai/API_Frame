

class CheckResult():

    @classmethod
    def is_equal(cls, response, expect_resp):
        expect_resp = eval(expect_resp)
        for resp in expect_resp:
            if resp not in response:
                return False
            else:
                if expect_resp[resp] != response[resp]:
                    return False
        return True