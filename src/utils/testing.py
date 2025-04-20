# some testing utilities

def run_tests(tests):
    """run a sequence of tests structured as a list of tuples: [(fn1, input_dict_1, output_1), etc. ]"""
    passed, failed = 0, 0
    for idx, test in enumerate(tests):
        try:
            fn, inputs, expected_output =  test
            observed_output = fn(**inputs) 
            if observed_output == expected_output:
                passed +=1
            else:
                print(f'Test {idx} failed.')
                print(f'Inputs: {inputs}')
                print(f"Expected Output: {expected_output}. Observed Output: {observed_output}.")
                failed +=1
        except Exception as e:
            print(f'Test {idx} failed with following error:')
            raise e
        
    print(f'Tests passed {passed}')
    print(f'Tests failed {failed}')