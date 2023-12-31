import pytest
from src.calculations import add,sub,BankAccount,InsufficientFunds

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)


@pytest.mark.parametrize("num1, num2, expected", [
    (3,2,5),(3,8,11),(12,4,16)
])
def test_add(num1,num2, expected):
    print("testing adding function")
    total = add(num1,num2)
    assert total == expected
    
    
    
def test_sub():
    print("testing subtracting function")
    assert sub(5,3) == 2 
    
    
def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance == 50
    
    
def test_bank_default_amount(zero_bank_account):

    assert  zero_bank_account.balance== 0
    
    
def test_withdraw(bank_account):

    bank_account.withdraw(20)
    assert bank_account.balance == 30
    
def test_deposit(bank_account):
  
    bank_account.deposit(20)
    assert bank_account.balance == 70
    
def test_collect_interest(bank_account):

    bank_account.collect_interest()
    assert round(bank_account.balance,2) == 55
    
@pytest.mark.parametrize("deposited, withdraw, expected", [
    (200,100,100),(300,150,150),(400,400,0)
])   
def test_bank_transaction(zero_bank_account,deposited, withdraw,expected):

        zero_bank_account.deposit(deposited)
    
        zero_bank_account.withdraw(withdraw)
        assert zero_bank_account.balance == expected
    
    
def test_insufficient_funds(zero_bank_account):
    with pytest.raises(InsufficientFunds):
        zero_bank_account.withdraw(200)