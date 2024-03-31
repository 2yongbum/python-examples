import dot

def test_dot():
  d = dot.Dot()
  d['a'] = 1
  d['b'] = 2
  assert d['a'] == 1
  assert d['b'] == 2
  assert d.a == 1
  d.c = 3
  assert d['c'] == 3

def test_dot2():
  d = dot.Dot()
  d.a.b.c = 1
  assert d.a.b.c == 1


def test_dot3():
  d = dot.Dot()
  d.a = dot.Dot()
  d.a.b.c = 1
  assert d.a.b.c == 1


def test_dot4():
  d = dot.Dot({'a': 1, 'b': 2})
  assert d.a == 1
  assert d.b == 2
  
