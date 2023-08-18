from employeers import Employee

def test_give_default_rise():
    """Test that a default rise works correctly."""
    employee = Employee('john', 10000)
    assert employee.give_rise() == 15000
