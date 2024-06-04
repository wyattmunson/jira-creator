commit_messages = [
    {
        'message': "Make change to data",
        'code_change': """
            def test_command():
                print("Created from array")
        """
    }
]

def get():
    return commit_messages