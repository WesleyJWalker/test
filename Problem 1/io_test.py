'''
Test cases for the io module.
'''
import input_output as io

class TestClass:
    def test_one(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        monkeypatch.setattr('builtins.input', lambda : "5")

        # go about using input() like you normally would:
        io.io_func()
        captured = capsys.readouterr()
        all_outputs = captured.out.split('\n')
        print(all_outputs)
        assert '5' not in all_outputs, "Make sure that the number is not printed"

    def test_two(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        monkeypatch.setattr('builtins.input', lambda : "6")

        # go about using input() like you normally would:
        io.io_func()
        captured = capsys.readouterr()
        all_outputs = captured.out.split('\n')
        print(all_outputs)
        assert 'x doubled is: 12' in all_outputs, "Make sure that the number is still doubled"