from src import operations as op

def test_add():
    assert op.add(4,3)==7
    assert op.add(2,-3)==-1

def test_sub():
    assert op.sub(4,3)==1
    assert op.sub(1,1)==0