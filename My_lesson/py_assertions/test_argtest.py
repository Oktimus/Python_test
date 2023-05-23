

def test_argtest01(CmdOpt):
   #print("REad config file:" + CmdOpt.readline())
    assert CmdOpt.readline().index('Lab')

