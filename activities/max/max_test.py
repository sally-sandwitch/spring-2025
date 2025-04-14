import max

def test_max():
    assert max.find_max([5])==0
    assert max.find_max([5.,10.,25.,0.])==2
    