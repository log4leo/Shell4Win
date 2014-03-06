
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\xce\x17\x7fg\x06\xa5\x06` M\xee\xb0\\7\x98\xa0'
    
_lr_action_items = {'LREDIRECT':([1,3,7,10,11,12,13,],[5,-7,-8,-5,5,-6,5,]),'PIPE':([1,3,7,10,12,],[6,-7,-8,-5,-6,]),'COLON':([1,3,7,10,12,],[9,-7,-8,-5,-6,]),'RREDIRECT':([1,3,7,10,11,12,13,],[8,-7,-8,-5,8,-6,8,]),'COMMAND':([0,1,3,5,6,7,8,9,10,11,12,13,],[3,7,-7,10,3,-8,12,3,-5,7,-6,7,]),'$end':([1,2,3,4,7,10,11,12,13,],[-2,0,-7,-1,-8,-5,-3,-6,-4,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'term':([0,6,9,],[1,11,13,]),'expression':([0,],[4,]),'statement':([0,],[2,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> expression','statement',1,'p_statement','C:\\Users\\Administrator\\Documents\\GitHub\\Shell4Win\\src\\tools.py',90),
  ('statement -> term','statement',1,'p_statement','C:\\Users\\Administrator\\Documents\\GitHub\\Shell4Win\\src\\tools.py',91),
  ('expression -> term PIPE term','expression',3,'p_expression_pipe','C:\\Users\\Administrator\\Documents\\GitHub\\Shell4Win\\src\\tools.py',98),
  ('expression -> term COLON term','expression',3,'p_expression_colon','C:\\Users\\Administrator\\Documents\\GitHub\\Shell4Win\\src\\tools.py',107),
  ('term -> term LREDIRECT COMMAND','term',3,'p_expression_lredirect','C:\\Users\\Administrator\\Documents\\GitHub\\Shell4Win\\src\\tools.py',115),
  ('term -> term RREDIRECT COMMAND','term',3,'p_expression_rredirect','C:\\Users\\Administrator\\Documents\\GitHub\\Shell4Win\\src\\tools.py',119),
  ('term -> COMMAND','term',1,'p_expression','C:\\Users\\Administrator\\Documents\\GitHub\\Shell4Win\\src\\tools.py',126),
  ('term -> term COMMAND','term',2,'p_expression','C:\\Users\\Administrator\\Documents\\GitHub\\Shell4Win\\src\\tools.py',127),
]
