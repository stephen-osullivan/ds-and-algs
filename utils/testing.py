# some testing utilities

def run_tests(fn, tests):
    passed, failed = 0, 0
    for idx, test in enumerate(tests):
        try:
            input = test['input']
            output = fn(**input) 
            if output == test['output']:
                print(f'Test {idx} passed.')
                passed +=1
            else:
                print(f'Test {idx} failed.')
                print(f'Inputs: {input}')
                print(f'Observed Output: {output}')
                print(f'Expected Output: {output}')
                failed +=1
        except Exception as e:
            print(f'Test {idx} failed with following error:')
            raise e
        
    print(f'Tests passed {passed}')
    print(f'Tests failed {failed}')