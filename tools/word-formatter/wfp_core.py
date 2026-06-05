# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.14.4 (main, Apr  8 2026, 04:02:31) [GCC 15.2.0]
# Embedded file name: wfp_core.py
"""Core document formatting engine for Word Formatter Pro v2.7.4.

This module is intentionally independent from Tkinter so GUI, CLI, and skills
can reuse the same formatter implementation. This copy is maintained for the
2.7.4 release.
"""
-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_come_froms ::= \e__come_froms COME_FROM . 
_come_froms ::= _come_froms . COME_FROM
_come_froms ::= _come_froms . COME_FROM_LOOP
_come_froms ::= _come_froms COME_FROM . 
_ifstmts_jump ::= COME_FROM . c_stmts come_froms
_ifstmts_jump ::= COME_FROM c_stmts . come_froms
_ifstmts_jump ::= COME_FROM c_stmts come_froms . 
_ifstmts_jump ::= \e_c_stmts_opt . COME_FROM
_ifstmts_jump ::= \e_c_stmts_opt . ELSE
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD \e__come_froms
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD _come_froms
_ifstmts_jump ::= \e_c_stmts_opt . come_froms
_ifstmts_jump ::= \e_c_stmts_opt COME_FROM . 
_ifstmts_jump ::= \e_c_stmts_opt come_froms . 
_ifstmts_jump ::= c_stmts_opt . COME_FROM
_ifstmts_jump ::= c_stmts_opt . ELSE
_ifstmts_jump ::= c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD \e__come_froms
_ifstmts_jump ::= c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD _come_froms
_ifstmts_jump ::= c_stmts_opt . come_froms
_ifstmts_jump ::= c_stmts_opt COME_FROM . 
_ifstmts_jump ::= c_stmts_opt come_froms . 
_ifstmts_jumpl ::= COME_FROM . c_stmts JUMP_BACK
_ifstmts_jumpl ::= COME_FROM . c_stmts JUMP_FORWARD
_ifstmts_jumpl ::= COME_FROM c_stmts . JUMP_BACK
_ifstmts_jumpl ::= COME_FROM c_stmts . JUMP_FORWARD
_ifstmts_jumpl ::= _ifstmts_jump . 
_ifstmts_jumpl ::= c_stmts . JUMP_BACK
_jump ::= JUMP_FORWARD . 
_stmts ::= _stmts . stmt
_stmts ::= _stmts stmt . 
_stmts ::= stmt . 
and ::= expr . JUMP_IF_FALSE_OR_POP expr \e_come_from_opt
and ::= expr . JUMP_IF_FALSE_OR_POP expr come_from_opt
and ::= expr . jifop_come_from expr
and ::= expr . jmp_false expr
and ::= expr . jmp_false expr COME_FROM
and ::= expr . jmp_false expr jmp_false
and ::= expr jmp_false . expr
and ::= expr jmp_false . expr COME_FROM
and ::= expr jmp_false . expr jmp_false
and ::= expr jmp_false expr . 
and ::= expr jmp_false expr . COME_FROM
and ::= expr jmp_false expr . jmp_false
and ::= expr jmp_false expr jmp_false . 
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false . expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false expr . POP_JUMP_IF_TRUE
and_not ::= expr jmp_false expr POP_JUMP_IF_TRUE . 
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true . LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true LOAD_GLOBAL . expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true LOAD_GLOBAL expr . CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 . RAISE_VARARGS_1
assert2 ::= expr jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1 . 
assert_invert ::= testtrue . LOAD_GLOBAL RAISE_VARARGS_1
assert_invert ::= testtrue LOAD_GLOBAL . RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign ::= expr store . 
assign2 ::= expr . expr ROT_TWO store store
assign2 ::= expr expr . ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr . expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr expr . ROT_THREE ROT_TWO store store store
async_for_stmt38 ::= expr . async_for store for_block COME_FROM_FINALLY END_ASYNC_FOR
async_forelse_stmt38 ::= expr . GET_AITER SETUP_FINALLY GET_ANEXT LOAD_CONST YIELD_FROM POP_BLOCK store for_block COME_FROM_FINALLY END_ASYNC_FOR else_suite
attribute ::= expr . LOAD_ATTR
attribute ::= expr LOAD_ATTR . 
attribute37 ::= expr . LOAD_METHOD
attribute37 ::= expr LOAD_METHOD . 
aug_assign1 ::= expr . expr inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr . expr inplace_op store
aug_assign1 ::= expr expr . inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr . inplace_op store
aug_assign2 ::= expr . DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
bin_op ::= expr expr . binary_operator
bin_op ::= expr expr binary_operator . 
binary_operator ::= BINARY_ADD . 
binary_operator ::= BINARY_TRUE_DIVIDE . 
break ::= POP_BLOCK . BREAK_LOOP
break ::= POP_BLOCK . POP_TOP BREAK_LOOP
break ::= POP_EXCEPT . BREAK_LOOP
break ::= POP_TOP . BREAK_LOOP
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= _stmts lastc_stmt . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_METHOD_0
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg CALL_METHOD_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg CALL_METHOD_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_METHOD_4
call ::= expr CALL_METHOD_0 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . CALL_METHOD_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg CALL_METHOD_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_METHOD_4
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg CALL_METHOD_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . CALL_METHOD_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_METHOD_4
call ::= expr pos_arg pos_arg CALL_FUNCTION_2 . 
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg . pos_arg CALL_METHOD_4
call ::= expr pos_arg pos_arg pos_arg pos_arg . CALL_METHOD_4
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr LOAD_CONST CALL_FUNCTION_KW_1 . 
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr LOAD_CONST CALL_FUNCTION_KW_2 . 
call_kw36 ::= expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7 . 
call_stmt ::= call . 
call_stmt ::= expr . POP_TOP
call_stmt ::= expr POP_TOP . 
cf_jf_else ::= come_froms . JUMP_FORWARD ELSE
cf_jump_back ::= COME_FROM . JUMP_BACK
cf_pt ::= COME_FROM . POP_TOP
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
come_from_opt ::= COME_FROM . 
come_froms ::= COME_FROM . 
come_froms ::= come_froms . COME_FROM
come_froms ::= come_froms COME_FROM . 
compare ::= compare_single . 
compare_chained ::= expr . compared_chained_middle ROT_TWO POP_TOP \e__come_froms
compare_chained ::= expr . compared_chained_middle ROT_TWO POP_TOP _come_froms
compare_chained37 ::= expr . compared_chained_middlea_37
compare_chained37 ::= expr . compared_chained_middlec_37
compare_chained37_false ::= expr . compare_chained_right_false_37
compare_chained37_false ::= expr . compared_chained_middle_false_37
compare_chained37_false ::= expr . compared_chained_middleb_false_37
compare_chained_right_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_righta_false_37 POP_TOP JUMP_BACK COME_FROM
compare_single ::= expr . expr COMPARE_OP
compare_single ::= expr expr . COMPARE_OP
compare_single ::= expr expr COMPARE_OP . 
compared_chained_middle ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained_right COME_FROM
compared_chained_middle ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compared_chained_middle COME_FROM
compared_chained_middle_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_rightb_false_37 POP_TOP _jump COME_FROM
compared_chained_middle_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_rightc_37 POP_TOP JUMP_FORWARD COME_FROM
compared_chained_middlea_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE
compared_chained_middlea_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_righta_37 COME_FROM POP_TOP COME_FROM
compared_chained_middleb_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_rightb_false_37 POP_TOP _jump COME_FROM
compared_chained_middlec_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_righta_37 POP_TOP
cond_except_stmts_opt ::= \e_cond_except_stmts_opt . cond_except_stmt
continue ::= POP_EXCEPT . JUMP_BACK
continues ::= _stmts . lastl_stmt continue
continues ::= _stmts lastl_stmt . continue
continues ::= lastl_stmt . continue
delete ::= DELETE_FAST . 
else_suite ::= suite_stmts . 
else_suitel ::= l_stmts . 
except_cond1 ::= DUP_TOP . expr COMPARE_OP jmp_false POP_TOP POP_TOP POP_TOP
except_cond1 ::= DUP_TOP . expr COMPARE_OP jmp_false POP_TOP POP_TOP POP_TOP POP_EXCEPT
except_cond1 ::= DUP_TOP expr . COMPARE_OP jmp_false POP_TOP POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr . COMPARE_OP jmp_false POP_TOP POP_TOP POP_TOP POP_EXCEPT
except_cond1 ::= DUP_TOP expr COMPARE_OP . jmp_false POP_TOP POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr COMPARE_OP . jmp_false POP_TOP POP_TOP POP_TOP POP_EXCEPT
except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false . POP_TOP POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false . POP_TOP POP_TOP POP_TOP POP_EXCEPT
except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP . POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP . POP_TOP POP_TOP POP_EXCEPT
except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP POP_TOP . POP_TOP
except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP POP_TOP . POP_TOP POP_EXCEPT
except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP POP_TOP POP_TOP . 
except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP POP_TOP POP_TOP . POP_EXCEPT
except_cond2 ::= DUP_TOP . expr COMPARE_OP jmp_false POP_TOP store POP_TOP \e_come_from_opt
except_cond2 ::= DUP_TOP . expr COMPARE_OP jmp_false POP_TOP store POP_TOP come_from_opt
except_cond2 ::= DUP_TOP expr . COMPARE_OP jmp_false POP_TOP store POP_TOP \e_come_from_opt
except_cond2 ::= DUP_TOP expr . COMPARE_OP jmp_false POP_TOP store POP_TOP come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP . jmp_false POP_TOP store POP_TOP \e_come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP . jmp_false POP_TOP store POP_TOP come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP jmp_false . POP_TOP store POP_TOP \e_come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP jmp_false . POP_TOP store POP_TOP come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP . store POP_TOP \e_come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP . store POP_TOP come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP store . POP_TOP \e_come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP store . POP_TOP come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP store POP_TOP . come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP store POP_TOP \e_come_from_opt . 
except_handler38 ::= _jump . COME_FROM_FINALLY except_stmts END_FINALLY \e_opt_come_from_except
except_handler38 ::= _jump . COME_FROM_FINALLY except_stmts END_FINALLY opt_come_from_except
except_handler38 ::= _jump COME_FROM_FINALLY . except_stmts END_FINALLY \e_opt_come_from_except
except_handler38 ::= _jump COME_FROM_FINALLY . except_stmts END_FINALLY opt_come_from_except
except_handler38 ::= _jump COME_FROM_FINALLY except_stmts . END_FINALLY \e_opt_come_from_except
except_handler38 ::= _jump COME_FROM_FINALLY except_stmts . END_FINALLY opt_come_from_except
except_handler38 ::= _jump COME_FROM_FINALLY except_stmts END_FINALLY . opt_come_from_except
except_handler38 ::= _jump COME_FROM_FINALLY except_stmts END_FINALLY \e_opt_come_from_except . 
except_handler38 ::= _jump COME_FROM_FINALLY except_stmts END_FINALLY opt_come_from_except . 
except_ret38 ::= SETUP_FINALLY . expr ROT_FOUR POP_BLOCK POP_EXCEPT CALL_FINALLY RETURN_VALUE COME_FROM COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
except_ret38 ::= SETUP_FINALLY . expr ROT_FOUR POP_BLOCK POP_EXCEPT CALL_FINALLY RETURN_VALUE COME_FROM COME_FROM_FINALLY suite_stmts_opt END_FINALLY
except_ret38 ::= SETUP_FINALLY expr . ROT_FOUR POP_BLOCK POP_EXCEPT CALL_FINALLY RETURN_VALUE COME_FROM COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
except_ret38 ::= SETUP_FINALLY expr . ROT_FOUR POP_BLOCK POP_EXCEPT CALL_FINALLY RETURN_VALUE COME_FROM COME_FROM_FINALLY suite_stmts_opt END_FINALLY
except_return_value ::= POP_BLOCK . return
except_return_value ::= POP_BLOCK return . 
except_return_value ::= expr . POP_BLOCK RETURN_VALUE
except_stmt ::= except_cond1 . except_suite \e_come_from_opt
except_stmt ::= except_cond1 . except_suite come_from_opt
except_stmt ::= except_cond1 except_suite . come_from_opt
except_stmt ::= except_cond1 except_suite \e_come_from_opt . 
except_stmt ::= except_cond1 except_suite come_from_opt . 
except_stmt ::= except_cond2 . except_suite \e_come_from_opt
except_stmt ::= except_cond2 . except_suite come_from_opt
except_stmt ::= except_cond2 . except_suite_finalize
except_stmt ::= except_cond2 except_suite . come_from_opt
except_stmt ::= except_cond2 except_suite \e_come_from_opt . 
except_stmt ::= except_cond2 except_suite come_from_opt . 
except_stmts ::= except_stmt . 
except_stmts ::= except_stmts . except_stmt
except_stmts ::= except_stmts except_stmt . 
except_suite ::= \e_c_stmts_opt . COME_FROM POP_EXCEPT jump_except COME_FROM
except_suite ::= \e_c_stmts_opt . POP_EXCEPT jump_except
except_suite ::= \e_c_stmts_opt . POP_EXCEPT jump_except ELSE
except_suite ::= c_stmts_opt . COME_FROM POP_EXCEPT jump_except COME_FROM
except_suite ::= c_stmts_opt . POP_EXCEPT jump_except
except_suite ::= c_stmts_opt . POP_EXCEPT jump_except ELSE
except_suite ::= c_stmts_opt POP_EXCEPT . jump_except
except_suite ::= c_stmts_opt POP_EXCEPT . jump_except ELSE
except_suite ::= c_stmts_opt POP_EXCEPT jump_except . 
except_suite ::= c_stmts_opt POP_EXCEPT jump_except . ELSE
except_suite_finalize ::= SETUP_FINALLY . c_stmts_opt except_var_finalize END_FINALLY _jump
except_suite_finalize ::= SETUP_FINALLY . returns COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY _jump
except_suite_finalize ::= SETUP_FINALLY . returns COME_FROM_FINALLY suite_stmts_opt END_FINALLY _jump
except_suite_finalize ::= SETUP_FINALLY \e_c_stmts_opt . except_var_finalize END_FINALLY _jump
except_suite_finalize ::= SETUP_FINALLY c_stmts_opt . except_var_finalize END_FINALLY _jump
except_var_finalize ::= POP_BLOCK . POP_EXCEPT LOAD_CONST COME_FROM_FINALLY LOAD_CONST store delete
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= and . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= bin_op . 
expr ::= call . 
expr ::= call_kw36 . 
expr ::= compare . 
expr ::= formatted_value1 . 
expr ::= formatted_value_debug . 
expr ::= joined_str . 
expr ::= list . 
expr ::= or . 
expr ::= subscript . 
expr ::= tuple . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jitop ::= expr JUMP_IF_TRUE_OR_POP . 
expr_jt ::= expr . jmp_true
expr_jt ::= expr jmp_true . 
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit ::= expr POP_JUMP_IF_TRUE . 
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_pjit_come_from ::= expr POP_JUMP_IF_TRUE . COME_FROM
expr_pjit_come_from ::= expr POP_JUMP_IF_TRUE COME_FROM . 
expr_stmt ::= expr . POP_TOP
expr_stmt ::= expr POP_TOP . 
for38 ::= expr . get_for_iter store for_block
for38 ::= expr . get_for_iter store for_block JUMP_BACK
for38 ::= expr . get_for_iter store for_block JUMP_BACK POP_BLOCK
for38 ::= expr . get_iter store for_block JUMP_BACK
forelselaststmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitec
forelselaststmtl38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitel
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_BACK \e__come_froms else_suite
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_BACK _come_froms else_suite
forelsestmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suite
formatted_value1 ::= expr . FORMAT_VALUE
formatted_value1 ::= expr FORMAT_VALUE . 
formatted_value_debug ::= LOAD_STR . formatted_value1 BUILD_STRING_2
formatted_value_debug ::= LOAD_STR . formatted_value1 LOAD_STR BUILD_STRING_3
formatted_value_debug ::= LOAD_STR . formatted_value2 BUILD_STRING_2
formatted_value_debug ::= LOAD_STR . formatted_value2 LOAD_STR BUILD_STRING_3
formatted_value_debug ::= LOAD_STR formatted_value1 . BUILD_STRING_2
formatted_value_debug ::= LOAD_STR formatted_value1 . LOAD_STR BUILD_STRING_3
formatted_value_debug ::= LOAD_STR formatted_value1 BUILD_STRING_2 . 
formatted_value_debug ::= LOAD_STR formatted_value1 LOAD_STR . BUILD_STRING_3
formatted_value_debug ::= LOAD_STR formatted_value1 LOAD_STR BUILD_STRING_3 . 
get_iter ::= expr . GET_ITER
if_exp ::= expr . jmp_false expr jf_cf expr COME_FROM
if_exp ::= expr . jmp_false expr jump_absolute_else expr
if_exp ::= expr jmp_false . expr jf_cf expr COME_FROM
if_exp ::= expr jmp_false . expr jump_absolute_else expr
if_exp ::= expr jmp_false expr . jf_cf expr COME_FROM
if_exp ::= expr jmp_false expr . jump_absolute_else expr
if_exp37 ::= expr . expr jf_cfs expr COME_FROM
if_exp37 ::= expr expr . jf_cfs expr COME_FROM
if_exp_37a ::= and_not . expr JUMP_FORWARD come_froms expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false . expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false expr . POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false expr POP_JUMP_IF_FALSE . jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false expr . return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not ::= expr jmp_true . expr jump_forward_else expr COME_FROM
if_exp_not ::= expr jmp_true expr . jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not_lambda ::= expr jmp_true . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not_lambda ::= expr jmp_true expr . return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_ret ::= expr . POP_JUMP_IF_FALSE expr RETURN_END_IF COME_FROM return_expr_or_cond
if_exp_true ::= expr . JUMP_FORWARD expr COME_FROM
ifelsestmt ::= testexpr . c_stmts come_froms else_suite come_froms
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt jf_cfs else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt jf_cfs else_suite opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt jump_forward_else else_suite \e__come_froms
ifelsestmt ::= testexpr . c_stmts_opt jump_forward_else else_suite _come_froms
ifelsestmt ::= testexpr . stmts jf_cfs \e_else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr . stmts jf_cfs \e_else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr . stmts jf_cfs else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr . stmts jf_cfs else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . jf_cfs else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . jf_cfs else_suite opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . jump_forward_else else_suite \e__come_froms
ifelsestmt ::= testexpr \e_c_stmts_opt . jump_forward_else else_suite _come_froms
ifelsestmt ::= testexpr c_stmts . come_froms else_suite come_froms
ifelsestmt ::= testexpr c_stmts come_froms . else_suite come_froms
ifelsestmt ::= testexpr c_stmts come_froms else_suite . come_froms
ifelsestmt ::= testexpr c_stmts come_froms else_suite come_froms . 
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jf_cfs else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jf_cfs else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jump_forward_else else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt . jump_forward_else else_suite _come_froms
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt opt_come_from_except
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt jump_absolute_else else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . jump_absolute_else else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . jump_absolute_else else_suitec
ifelsestmtl ::= testexpr . c_stmts cf_pt else_suite
ifelsestmtl ::= testexpr . c_stmts_opt cf_jf_else else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt cf_jump_back else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt jb_cfs else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt jb_cfs else_suitel JUMP_BACK come_froms
ifelsestmtl ::= testexpr . c_stmts_opt jb_else else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt jump_forward_else else_suitec
ifelsestmtl ::= testexpr \e_c_stmts_opt . cf_jf_else else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . cf_jump_back else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . jb_cfs else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . jb_cfs else_suitel JUMP_BACK come_froms
ifelsestmtl ::= testexpr \e_c_stmts_opt . jb_else else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . jump_forward_else else_suitec
ifelsestmtl ::= testexpr c_stmts . cf_pt else_suite
ifelsestmtl ::= testexpr c_stmts_opt . cf_jf_else else_suitel
ifelsestmtl ::= testexpr c_stmts_opt . cf_jump_back else_suitel
ifelsestmtl ::= testexpr c_stmts_opt . jb_cfs else_suitel
ifelsestmtl ::= testexpr c_stmts_opt . jb_cfs else_suitel JUMP_BACK come_froms
ifelsestmtl ::= testexpr c_stmts_opt . jb_else else_suitel
ifelsestmtl ::= testexpr c_stmts_opt . jump_forward_else else_suitec
ifelsestmtl ::= testexpr_cf . c_stmts_opt jb_else else_suitel
ifelsestmtl ::= testexpr_cf \e_c_stmts_opt . jb_else else_suitel
ifelsestmtl ::= testexpr_cf c_stmts_opt . jb_else else_suitel
ifelsestmtr ::= testexpr . return_if_stmts returns
iflaststmt ::= testexpr . c_stmts
iflaststmt ::= testexpr . c_stmts JUMP_ABSOLUTE
iflaststmt ::= testexpr . c_stmts_opt JUMP_FORWARD
iflaststmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD
iflaststmt ::= testexpr c_stmts . 
iflaststmt ::= testexpr c_stmts . JUMP_ABSOLUTE
iflaststmt ::= testexpr c_stmts_opt . JUMP_FORWARD
iflaststmtl ::= testexpr . c_stmts
iflaststmtl ::= testexpr . c_stmts JUMP_BACK
iflaststmtl ::= testexpr . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexpr . c_stmts JUMP_BACK POP_BLOCK
iflaststmtl ::= testexpr c_stmts . 
iflaststmtl ::= testexpr c_stmts . JUMP_BACK
iflaststmtl ::= testexpr c_stmts . JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexpr c_stmts . JUMP_BACK POP_BLOCK
iflaststmtl ::= testexprl . c_stmts JUMP_BACK
iflaststmtl ::= testexprl . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexprl . c_stmts JUMP_BACK POP_BLOCK
iflaststmtl ::= testexprl c_stmts . JUMP_BACK
iflaststmtl ::= testexprl c_stmts . JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexprl c_stmts . JUMP_BACK POP_BLOCK
ifpoplaststmtl ::= testexpr . POP_TOP \e_c_stmts_opt
ifpoplaststmtl ::= testexpr . POP_TOP c_stmts_opt
ifstmt ::= testexpr . _ifstmts_jump
ifstmt ::= testexpr _ifstmts_jump . 
ifstmtl ::= testexpr . _ifstmts_jumpl
ifstmtl ::= testexpr _ifstmts_jumpl . 
import ::= LOAD_CONST . LOAD_CONST alias
import_as37 ::= LOAD_CONST . LOAD_CONST importlist37 store POP_TOP
import_from ::= LOAD_CONST . LOAD_CONST IMPORT_NAME importlist POP_TOP
import_from ::= LOAD_CONST . LOAD_CONST importlist POP_TOP
import_from37 ::= LOAD_CONST . LOAD_CONST IMPORT_NAME_ATTR importlist37 POP_TOP
import_from_as37 ::= LOAD_CONST . LOAD_CONST import_from_attr37 store POP_TOP
import_from_star ::= LOAD_CONST . LOAD_CONST IMPORT_NAME IMPORT_STAR
import_from_star ::= LOAD_CONST . LOAD_CONST IMPORT_NAME_ATTR IMPORT_STAR
importmultiple ::= LOAD_CONST . LOAD_CONST alias imports_cont
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
joined_str ::= expr . expr BUILD_STRING_2
joined_str ::= expr . expr expr BUILD_STRING_3
joined_str ::= expr . expr expr expr BUILD_STRING_4
joined_str ::= expr expr . BUILD_STRING_2
joined_str ::= expr expr . expr BUILD_STRING_3
joined_str ::= expr expr . expr expr BUILD_STRING_4
joined_str ::= expr expr BUILD_STRING_2 . 
joined_str ::= expr expr expr . BUILD_STRING_3
joined_str ::= expr expr expr . expr BUILD_STRING_4
joined_str ::= expr expr expr BUILD_STRING_3 . 
joined_str ::= expr expr expr expr . BUILD_STRING_4
joined_str ::= expr expr expr expr BUILD_STRING_4 . 
jump_absolute_else ::= come_froms . _jump COME_FROM
jump_except ::= JUMP_FORWARD . 
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= _stmts lastl_stmt . 
l_stmts ::= l_stmts . lstmt
l_stmts ::= l_stmts lstmt . 
l_stmts ::= lastl_stmt . 
l_stmts ::= lastl_stmt . come_froms l_stmts
l_stmts ::= lastl_stmt come_froms . l_stmts
l_stmts ::= lastl_stmt come_froms l_stmts . 
l_stmts ::= lstmt . 
l_stmts ::= returns . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= iflaststmtl . 
lc_setup_finally ::= LOAD_CONST . SETUP_FINALLY
list ::= expr . expr BUILD_LIST_2
list ::= expr . expr expr BUILD_LIST_3
list ::= expr . expr expr expr expr expr expr expr expr BUILD_LIST_9
list ::= expr expr . BUILD_LIST_2
list ::= expr expr . expr BUILD_LIST_3
list ::= expr expr . expr expr expr expr expr expr expr BUILD_LIST_9
list ::= expr expr expr . BUILD_LIST_3
list ::= expr expr expr . expr expr expr expr expr expr BUILD_LIST_9
list ::= expr expr expr expr . expr expr expr expr expr BUILD_LIST_9
list ::= expr expr expr expr expr . expr expr expr expr BUILD_LIST_9
list ::= expr expr expr expr expr expr . expr expr expr BUILD_LIST_9
list ::= expr expr expr expr expr expr expr . expr expr BUILD_LIST_9
list ::= expr expr expr expr expr expr expr expr . expr BUILD_LIST_9
list ::= expr expr expr expr expr expr expr expr expr . BUILD_LIST_9
list ::= expr expr expr expr expr expr expr expr expr BUILD_LIST_9 . 
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
named_expr ::= expr . DUP_TOP store
opt_come_from_except ::= _come_froms . 
or ::= and . jitop_come_from_expr COME_FROM
or ::= expr_jitop . expr COME_FROM
or ::= expr_jitop expr . COME_FROM
or ::= expr_jitop expr COME_FROM . 
or ::= expr_jt . expr
or ::= expr_jt . expr COME_FROM
or ::= expr_jt expr . 
or ::= expr_jt expr . COME_FROM
or ::= expr_pjit . expr POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr . POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit_come_from . expr
or ::= expr_pjit_come_from expr . 
pop_ex_return ::= return_expr . ROT_FOUR POP_EXCEPT RETURN_VALUE
pop_return ::= POP_TOP . return_expr RETURN_VALUE
popb_return ::= return_expr . POP_BLOCK RETURN_VALUE
pos_arg ::= expr . 
raise_stmt0 ::= RAISE_VARARGS_0 . 
raise_stmt1 ::= expr . RAISE_VARARGS_1
raise_stmt1 ::= expr RAISE_VARARGS_1 . 
raise_stmt2 ::= expr . expr RAISE_VARARGS_2
raise_stmt2 ::= expr expr . RAISE_VARARGS_2
raise_stmt2 ::= expr expr RAISE_VARARGS_2 . 
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr JUMP_IF_TRUE_OR_POP . return_expr_or_cond COME_FROM
ret_or ::= expr JUMP_IF_TRUE_OR_POP return_expr_or_cond . COME_FROM
ret_or ::= expr JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM . 
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return ::= return_expr . discard_tops RETURN_VALUE
return ::= return_expr RETURN_VALUE . 
return ::= return_expr RETURN_VALUE . COME_FROM
return ::= return_expr RETURN_VALUE COME_FROM . 
return_except ::= stmts . POP_BLOCK return
return_except ::= stmts POP_BLOCK . return
return_except ::= stmts POP_BLOCK return . 
return_expr ::= expr . 
return_expr ::= ret_or . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_expr_or_cond ::= return_expr . 
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr . RETURN_END_IF POP_BLOCK
return_if_stmts ::= _stmts . return_if_stmt \e__come_froms
return_if_stmts ::= _stmts . return_if_stmt _come_froms
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
returns ::= _stmts return . 
returns ::= return . 
returns_in_except ::= _stmts . except_return_value
returns_in_except ::= _stmts except_return_value . 
sf_pb_call_returns ::= SETUP_FINALLY . POP_BLOCK CALL_FINALLY returns
sstmt ::= return . RETURN_LAST
sstmt ::= return RETURN_LAST . 
sstmt ::= sstmt . RETURN_LAST
sstmt ::= sstmt RETURN_LAST . 
sstmt ::= stmt . 
stmt ::= assert2 . 
stmt ::= assign . 
stmt ::= call_stmt . 
stmt ::= delete . 
stmt ::= expr_stmt . 
stmt ::= ifelsestmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= raise_stmt0 . 
stmt ::= raise_stmt1 . 
stmt ::= raise_stmt2 . 
stmt ::= return . 
stmt ::= try_elsestmtl38 . 
stmt ::= try_except . 
stmt ::= tryfinallystmt . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript ::= expr expr BINARY_SUBSCR . 
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
suite_stmts ::= _stmts . 
suite_stmts ::= returns . 
suite_stmts_opt ::= suite_stmts . 
testexpr ::= testfalse . 
testexpr ::= testtrue . 
testexpr_cf ::= testexpr . come_froms
testexpr_cf ::= testexpr come_froms . 
testexprl ::= testfalsel . 
testfalse ::= and_not . 
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse ::= or . jmp_false COME_FROM
testfalse ::= testfalse_not_and . 
testfalse_not_and ::= and . jmp_true come_froms
testfalse_not_and ::= and jmp_true . come_froms
testfalse_not_and ::= and jmp_true come_froms . 
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr jmp_true . COME_FROM
testfalse_not_and ::= expr jmp_false expr jmp_true COME_FROM . 
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr . jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr jmp_false . COME_FROM
testfalsel ::= expr . jmp_true
testfalsel ::= expr jmp_true . 
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
try_elsestmtl38 ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK except_handler38 COME_FROM else_suitel \e_opt_come_from_except
try_elsestmtl38 ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK except_handler38 COME_FROM else_suitel opt_come_from_except
try_elsestmtl38 ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK except_handler38 COME_FROM else_suitel \e_opt_come_from_except
try_elsestmtl38 ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK except_handler38 COME_FROM else_suitel opt_come_from_except
try_elsestmtl38 ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK except_handler38 COME_FROM else_suitel \e_opt_come_from_except
try_elsestmtl38 ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK except_handler38 COME_FROM else_suitel opt_come_from_except
try_elsestmtl38 ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK . except_handler38 COME_FROM else_suitel \e_opt_come_from_except
try_elsestmtl38 ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK . except_handler38 COME_FROM else_suitel opt_come_from_except
try_elsestmtl38 ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK except_handler38 . COME_FROM else_suitel \e_opt_come_from_except
try_elsestmtl38 ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK except_handler38 . COME_FROM else_suitel opt_come_from_except
try_elsestmtl38 ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK except_handler38 COME_FROM . else_suitel \e_opt_come_from_except
try_elsestmtl38 ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK except_handler38 COME_FROM . else_suitel opt_come_from_except
try_elsestmtl38 ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK except_handler38 COME_FROM else_suitel . opt_come_from_except
try_elsestmtl38 ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK except_handler38 COME_FROM else_suitel \e_opt_come_from_except . 
try_elsestmtl38 ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK except_handler38 COME_FROM else_suitel opt_come_from_except . 
try_except ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK except_handler38
try_except ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK except_handler38
try_except ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK except_handler38
try_except ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK . except_handler38
try_except ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK except_handler38 . 
try_except38 ::= SETUP_FINALLY . POP_BLOCK POP_TOP \e_suite_stmts_opt except_handler38a
try_except38 ::= SETUP_FINALLY . POP_BLOCK POP_TOP suite_stmts_opt except_handler38a
try_except38 ::= SETUP_FINALLY . POP_BLOCK suite_stmts except_handler38b
try_except38r ::= SETUP_FINALLY . return_except except_handler38b
try_except38r ::= SETUP_FINALLY return_except . except_handler38b
try_except38r2 ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP \e_cond_except_stmts_opt POP_EXCEPT return END_FINALLY COME_FROM
try_except38r2 ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP cond_except_stmts_opt POP_EXCEPT return END_FINALLY COME_FROM
try_except38r2 ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP \e_cond_except_stmts_opt POP_EXCEPT return END_FINALLY COME_FROM
try_except38r2 ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP cond_except_stmts_opt POP_EXCEPT return END_FINALLY COME_FROM
try_except38r2 ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP \e_cond_except_stmts_opt POP_EXCEPT return END_FINALLY COME_FROM
try_except38r2 ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP cond_except_stmts_opt POP_EXCEPT return END_FINALLY COME_FROM
try_except38r2 ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK . JUMP_FORWARD COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP \e_cond_except_stmts_opt POP_EXCEPT return END_FINALLY COME_FROM
try_except38r2 ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK . JUMP_FORWARD COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP cond_except_stmts_opt POP_EXCEPT return END_FINALLY COME_FROM
try_except38r2 ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK JUMP_FORWARD . COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP \e_cond_except_stmts_opt POP_EXCEPT return END_FINALLY COME_FROM
try_except38r2 ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK JUMP_FORWARD . COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP cond_except_stmts_opt POP_EXCEPT return END_FINALLY COME_FROM
try_except38r2 ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY . POP_TOP POP_TOP POP_TOP \e_cond_except_stmts_opt POP_EXCEPT return END_FINALLY COME_FROM
try_except38r2 ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY . POP_TOP POP_TOP POP_TOP cond_except_stmts_opt POP_EXCEPT return END_FINALLY COME_FROM
try_except38r3 ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY \e_cond_except_stmts_opt POP_EXCEPT return COME_FROM END_FINALLY COME_FROM
try_except38r3 ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY cond_except_stmts_opt POP_EXCEPT return COME_FROM END_FINALLY COME_FROM
try_except38r3 ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY \e_cond_except_stmts_opt POP_EXCEPT return COME_FROM END_FINALLY COME_FROM
try_except38r3 ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY cond_except_stmts_opt POP_EXCEPT return COME_FROM END_FINALLY COME_FROM
try_except38r3 ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY \e_cond_except_stmts_opt POP_EXCEPT return COME_FROM END_FINALLY COME_FROM
try_except38r3 ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY cond_except_stmts_opt POP_EXCEPT return COME_FROM END_FINALLY COME_FROM
try_except38r3 ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK . JUMP_FORWARD COME_FROM_FINALLY \e_cond_except_stmts_opt POP_EXCEPT return COME_FROM END_FINALLY COME_FROM
try_except38r3 ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK . JUMP_FORWARD COME_FROM_FINALLY cond_except_stmts_opt POP_EXCEPT return COME_FROM END_FINALLY COME_FROM
try_except38r3 ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK JUMP_FORWARD . COME_FROM_FINALLY \e_cond_except_stmts_opt POP_EXCEPT return COME_FROM END_FINALLY COME_FROM
try_except38r3 ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK JUMP_FORWARD . COME_FROM_FINALLY cond_except_stmts_opt POP_EXCEPT return COME_FROM END_FINALLY COME_FROM
try_except38r3 ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY . cond_except_stmts_opt POP_EXCEPT return COME_FROM END_FINALLY COME_FROM
try_except38r3 ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY \e_cond_except_stmts_opt . POP_EXCEPT return COME_FROM END_FINALLY COME_FROM
try_except38r4 ::= SETUP_FINALLY . returns_in_except COME_FROM_FINALLY except_cond1 return COME_FROM END_FINALLY
try_except38r4 ::= SETUP_FINALLY returns_in_except . COME_FROM_FINALLY except_cond1 return COME_FROM END_FINALLY
try_except38r4 ::= SETUP_FINALLY returns_in_except COME_FROM_FINALLY . except_cond1 return COME_FROM END_FINALLY
try_except_as ::= SETUP_FINALLY . POP_BLOCK suite_stmts except_handler_as END_FINALLY COME_FROM
try_except_as ::= SETUP_FINALLY . suite_stmts except_handler_as END_FINALLY COME_FROM
try_except_as ::= SETUP_FINALLY suite_stmts . except_handler_as END_FINALLY COME_FROM
try_except_ret38 ::= SETUP_FINALLY . returns except_ret38a
tryfinally36 ::= SETUP_FINALLY . returns COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinally36 ::= SETUP_FINALLY . returns COME_FROM_FINALLY suite_stmts
tryfinally36 ::= SETUP_FINALLY . returns COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinally38astmt ::= LOAD_CONST . SETUP_FINALLY \e_suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY POP_TOP \e_suite_stmts_opt END_FINALLY POP_TOP
tryfinally38astmt ::= LOAD_CONST . SETUP_FINALLY \e_suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY POP_TOP suite_stmts_opt END_FINALLY POP_TOP
tryfinally38astmt ::= LOAD_CONST . SETUP_FINALLY suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY POP_TOP \e_suite_stmts_opt END_FINALLY POP_TOP
tryfinally38astmt ::= LOAD_CONST . SETUP_FINALLY suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY POP_TOP suite_stmts_opt END_FINALLY POP_TOP
tryfinally38rstmt3 ::= SETUP_FINALLY . expr POP_BLOCK CALL_FINALLY RETURN_VALUE COME_FROM COME_FROM_FINALLY ss_end_finally
tryfinally38rstmt3 ::= SETUP_FINALLY expr . POP_BLOCK CALL_FINALLY RETURN_VALUE COME_FROM COME_FROM_FINALLY ss_end_finally
tryfinally38stmt ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK . BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK . BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK BEGIN_FINALLY . COME_FROM_FINALLY POP_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK BEGIN_FINALLY . COME_FROM_FINALLY POP_FINALLY suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY . POP_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY . POP_FINALLY suite_stmts_opt END_FINALLY
tryfinally_return_stmt ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_FINALLY
tryfinally_return_stmt ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_FINALLY
tryfinally_return_stmt ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_FINALLY
tryfinally_return_stmt ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK . LOAD_CONST COME_FROM_FINALLY
tryfinally_return_stmt ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK LOAD_CONST . COME_FROM_FINALLY
tryfinallystmt ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK . BEGIN_FINALLY COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK . BEGIN_FINALLY COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK . LOAD_CONST COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK . LOAD_CONST COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK BEGIN_FINALLY . COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK BEGIN_FINALLY . COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY . suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY \e_suite_stmts_opt . END_FINALLY
tryfinallystmt ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY suite_stmts_opt . END_FINALLY
tryfinallystmt ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY suite_stmts_opt END_FINALLY . 
tryfinallystmt ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK LOAD_CONST . COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK LOAD_CONST . COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr BUILD_TUPLE_2 . 
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
while1stmt ::= \e__come_froms . l_stmts COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= \e__come_froms l_stmts . COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= \e__come_froms l_stmts COME_FROM . JUMP_BACK COME_FROM_LOOP
while1stmt ::= _come_froms . l_stmts COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= _come_froms l_stmts . COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= _come_froms l_stmts COME_FROM . JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= \e__come_froms . l_stmts JUMP_BACK POP_BLOCK
whileTruestmt ::= \e__come_froms l_stmts . JUMP_BACK POP_BLOCK
whileTruestmt ::= _come_froms . l_stmts JUMP_BACK POP_BLOCK
whileTruestmt ::= _come_froms l_stmts . JUMP_BACK POP_BLOCK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= \e__come_froms . pass JUMP_BACK
whileTruestmt38 ::= \e__come_froms \e_pass . JUMP_BACK
whileTruestmt38 ::= \e__come_froms l_stmts . JUMP_BACK
whileTruestmt38 ::= \e__come_froms l_stmts . JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= _come_froms . l_stmts JUMP_BACK
whileTruestmt38 ::= _come_froms . l_stmts JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= _come_froms . pass JUMP_BACK
whileTruestmt38 ::= _come_froms \e_pass . JUMP_BACK
whileTruestmt38 ::= _come_froms l_stmts . JUMP_BACK
whileTruestmt38 ::= _come_froms l_stmts . JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts JUMP_BACK
whilestmt38 ::= \e__come_froms . testexpr l_stmts come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr returns POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr . l_stmts JUMP_BACK
whilestmt38 ::= \e__come_froms testexpr . l_stmts come_froms
whilestmt38 ::= \e__come_froms testexpr . l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr . l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr . l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms testexpr . returns POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr \e_l_stmts_opt . COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr \e_l_stmts_opt . JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr \e_l_stmts_opt . JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms testexpr \e_l_stmts_opt COME_FROM . JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr l_stmts . JUMP_BACK
whilestmt38 ::= \e__come_froms testexpr l_stmts . come_froms
whilestmt38 ::= \e__come_froms testexpr l_stmts come_froms . 
whilestmt38 ::= \e__come_froms testexpr l_stmts_opt . COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr l_stmts_opt . JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr l_stmts_opt . JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms testexpr l_stmts_opt COME_FROM . JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr returns . POP_BLOCK
whilestmt38 ::= _come_froms . testexpr \e_l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= _come_froms . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= _come_froms . testexpr \e_l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= _come_froms . testexpr l_stmts JUMP_BACK
whilestmt38 ::= _come_froms . testexpr l_stmts come_froms
whilestmt38 ::= _come_froms . testexpr l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= _come_froms . testexpr l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= _come_froms . testexpr l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= _come_froms . testexpr returns POP_BLOCK
whilestmt38 ::= _come_froms testexpr . l_stmts JUMP_BACK
whilestmt38 ::= _come_froms testexpr . l_stmts come_froms
whilestmt38 ::= _come_froms testexpr . l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= _come_froms testexpr . l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= _come_froms testexpr . l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= _come_froms testexpr . returns POP_BLOCK
whilestmt38 ::= _come_froms testexpr \e_l_stmts_opt . COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= _come_froms testexpr \e_l_stmts_opt . JUMP_BACK POP_BLOCK
whilestmt38 ::= _come_froms testexpr \e_l_stmts_opt . JUMP_BACK come_froms
whilestmt38 ::= _come_froms testexpr l_stmts . JUMP_BACK
whilestmt38 ::= _come_froms testexpr l_stmts . come_froms
whilestmt38 ::= _come_froms testexpr l_stmts come_froms . 
whilestmt38 ::= _come_froms testexpr l_stmts_opt . COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= _come_froms testexpr l_stmts_opt . JUMP_BACK POP_BLOCK
whilestmt38 ::= _come_froms testexpr l_stmts_opt . JUMP_BACK come_froms
whilestmt38 ::= _come_froms testexpr l_stmts_opt COME_FROM . JUMP_BACK POP_BLOCK
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
-> 
 L. 231         0  LOAD_GLOBAL              IS_WINDOWS
                   2  POP_JUMP_IF_FALSE    12  'to 12'
                   4  LOAD_GLOBAL              pythoncom
                   6  LOAD_CONST               None
                   8  COMPARE_OP               is-not
                  10  POP_JUMP_IF_TRUE     16  'to 16'
                12_0  COME_FROM             2  '2'

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_come_froms ::= \e__come_froms COME_FROM . 
_come_froms ::= _come_froms . COME_FROM
_come_froms ::= _come_froms . COME_FROM_LOOP
_ifstmts_jump ::= \e_c_stmts_opt . COME_FROM
_ifstmts_jump ::= \e_c_stmts_opt . ELSE
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD \e__come_froms
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD _come_froms
_ifstmts_jump ::= \e_c_stmts_opt . come_froms
_ifstmts_jump ::= c_stmts_opt . COME_FROM
_ifstmts_jump ::= c_stmts_opt . ELSE
_ifstmts_jump ::= c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD \e__come_froms
_ifstmts_jump ::= c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD _come_froms
_ifstmts_jump ::= c_stmts_opt . come_froms
_ifstmts_jumpl ::= c_stmts . JUMP_BACK
_stmts ::= _stmts . stmt
_stmts ::= _stmts stmt . 
_stmts ::= stmt . 
add_consts ::= \e_add_consts . ADD_VALUE
add_consts ::= \e_add_consts ADD_VALUE . 
add_consts ::= add_consts . ADD_VALUE
add_consts ::= add_consts ADD_VALUE . 
and ::= expr . JUMP_IF_FALSE_OR_POP expr \e_come_from_opt
and ::= expr . JUMP_IF_FALSE_OR_POP expr come_from_opt
and ::= expr . jifop_come_from expr
and ::= expr . jmp_false expr
and ::= expr . jmp_false expr COME_FROM
and ::= expr . jmp_false expr jmp_false
and ::= expr JUMP_IF_FALSE_OR_POP . expr \e_come_from_opt
and ::= expr JUMP_IF_FALSE_OR_POP . expr come_from_opt
and ::= expr JUMP_IF_FALSE_OR_POP expr . come_from_opt
and ::= expr JUMP_IF_FALSE_OR_POP expr \e_come_from_opt . 
and ::= expr JUMP_IF_FALSE_OR_POP expr come_from_opt . 
and ::= expr jmp_false . expr
and ::= expr jmp_false . expr COME_FROM
and ::= expr jmp_false . expr jmp_false
and ::= expr jmp_false expr . 
and ::= expr jmp_false expr . COME_FROM
and ::= expr jmp_false expr . jmp_false
and ::= expr jmp_false expr COME_FROM . 
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false . expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false expr . POP_JUMP_IF_TRUE
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true . LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert_invert ::= testtrue . LOAD_GLOBAL RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign ::= expr store . 
assign2 ::= expr . expr ROT_TWO store store
assign2 ::= expr expr . ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr . expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr expr . ROT_THREE ROT_TWO store store store
async_for_stmt38 ::= expr . async_for store for_block COME_FROM_FINALLY END_ASYNC_FOR
async_forelse_stmt38 ::= expr . GET_AITER SETUP_FINALLY GET_ANEXT LOAD_CONST YIELD_FROM POP_BLOCK store for_block COME_FROM_FINALLY END_ASYNC_FOR else_suite
attribute ::= expr . LOAD_ATTR
attribute37 ::= expr . LOAD_METHOD
attribute37 ::= expr LOAD_METHOD . 
aug_assign1 ::= expr . expr inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr . expr inplace_op store
aug_assign1 ::= expr expr . inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr . inplace_op store
aug_assign2 ::= expr . DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
bin_op ::= expr expr . binary_operator
bin_op ::= expr expr binary_operator . 
binary_operator ::= BINARY_ADD . 
binary_operator ::= BINARY_SUBTRACT . 
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_METHOD_0
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg CALL_METHOD_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg CALL_METHOD_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_METHOD_4
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . CALL_METHOD_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg CALL_METHOD_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_METHOD_4
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . CALL_METHOD_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_METHOD_4
call ::= expr pos_arg pos_arg CALL_METHOD_2 . 
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_stmt ::= call . 
call_stmt ::= expr . POP_TOP
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
come_from_loops ::= \e_come_from_loops . COME_FROM_LOOP
come_from_opt ::= COME_FROM . 
come_froms ::= COME_FROM . 
come_froms ::= come_froms . COME_FROM
come_froms ::= come_froms COME_FROM . 
compare ::= compare_single . 
compare_chained ::= expr . compared_chained_middle ROT_TWO POP_TOP \e__come_froms
compare_chained ::= expr . compared_chained_middle ROT_TWO POP_TOP _come_froms
compare_chained37 ::= expr . compared_chained_middlea_37
compare_chained37 ::= expr . compared_chained_middlec_37
compare_chained37_false ::= expr . compare_chained_right_false_37
compare_chained37_false ::= expr . compared_chained_middle_false_37
compare_chained37_false ::= expr . compared_chained_middleb_false_37
compare_chained_right_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_righta_false_37 POP_TOP JUMP_BACK COME_FROM
compare_single ::= expr . expr COMPARE_OP
compare_single ::= expr expr . COMPARE_OP
compare_single ::= expr expr COMPARE_OP . 
compared_chained_middle ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained_right COME_FROM
compared_chained_middle ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compared_chained_middle COME_FROM
compared_chained_middle_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_rightb_false_37 POP_TOP _jump COME_FROM
compared_chained_middle_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_rightc_37 POP_TOP JUMP_FORWARD COME_FROM
compared_chained_middlea_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE
compared_chained_middlea_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_righta_37 COME_FROM POP_TOP COME_FROM
compared_chained_middleb_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_rightb_false_37 POP_TOP _jump COME_FROM
compared_chained_middlec_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_righta_37 POP_TOP
const_list ::= COLLECTION_START . add_consts BUILD_CONST_DICT
const_list ::= COLLECTION_START . add_consts BUILD_CONST_LIST
const_list ::= COLLECTION_START \e_add_consts . BUILD_CONST_DICT
const_list ::= COLLECTION_START \e_add_consts . BUILD_CONST_LIST
const_list ::= COLLECTION_START add_consts . BUILD_CONST_DICT
const_list ::= COLLECTION_START add_consts . BUILD_CONST_LIST
const_list ::= COLLECTION_START add_consts BUILD_CONST_DICT . 
continues ::= _stmts . lastl_stmt continue
continues ::= _stmts lastl_stmt . continue
continues ::= lastl_stmt . continue
dict ::= const_list . 
else_suitel ::= l_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= and . 
expr ::= attribute37 . 
expr ::= bin_op . 
expr ::= call . 
expr ::= compare . 
expr ::= const_list . 
expr ::= dict . 
expr ::= get_iter . 
expr ::= or . 
expr ::= subscript . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_jt ::= expr jmp_true . 
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit ::= expr POP_JUMP_IF_TRUE . 
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_pjit_come_from ::= expr POP_JUMP_IF_TRUE . COME_FROM
expr_stmt ::= expr . POP_TOP
for38 ::= expr . get_for_iter store for_block
for38 ::= expr . get_for_iter store for_block JUMP_BACK
for38 ::= expr . get_for_iter store for_block JUMP_BACK POP_BLOCK
for38 ::= expr . get_iter store for_block JUMP_BACK
for38 ::= expr get_for_iter . store for_block
for38 ::= expr get_for_iter . store for_block JUMP_BACK
for38 ::= expr get_for_iter . store for_block JUMP_BACK POP_BLOCK
for38 ::= expr get_for_iter store . for_block
for38 ::= expr get_for_iter store . for_block JUMP_BACK
for38 ::= expr get_for_iter store . for_block JUMP_BACK POP_BLOCK
for_block ::= \e__come_froms . l_stmts_opt _come_from_loops JUMP_BACK
for_block ::= \e__come_froms \e_l_stmts_opt . _come_from_loops JUMP_BACK
for_block ::= \e_l_stmts_opt . _come_froms JUMP_BACK
for_block ::= \e_l_stmts_opt . come_from_loops JUMP_BACK
for_block ::= \e_l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= \e_l_stmts_opt \e_come_from_loops . JUMP_BACK
forelselaststmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitec
forelselaststmt38 ::= expr get_for_iter . store for_block POP_BLOCK else_suitec
forelselaststmt38 ::= expr get_for_iter store . for_block POP_BLOCK else_suitec
forelselaststmtl38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitel
forelselaststmtl38 ::= expr get_for_iter . store for_block POP_BLOCK else_suitel
forelselaststmtl38 ::= expr get_for_iter store . for_block POP_BLOCK else_suitel
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_BACK \e__come_froms else_suite
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_BACK _come_froms else_suite
forelsestmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suite
forelsestmt38 ::= expr get_for_iter . store for_block JUMP_BACK \e__come_froms else_suite
forelsestmt38 ::= expr get_for_iter . store for_block JUMP_BACK _come_froms else_suite
forelsestmt38 ::= expr get_for_iter . store for_block POP_BLOCK else_suite
forelsestmt38 ::= expr get_for_iter store . for_block JUMP_BACK \e__come_froms else_suite
forelsestmt38 ::= expr get_for_iter store . for_block JUMP_BACK _come_froms else_suite
forelsestmt38 ::= expr get_for_iter store . for_block POP_BLOCK else_suite
formatted_value1 ::= expr . FORMAT_VALUE
get_for_iter ::= GET_ITER . _come_froms FOR_ITER
get_for_iter ::= GET_ITER \e__come_froms . FOR_ITER
get_for_iter ::= GET_ITER _come_froms . FOR_ITER
get_for_iter ::= GET_ITER _come_froms FOR_ITER . 
get_iter ::= expr . GET_ITER
get_iter ::= expr GET_ITER . 
if_exp ::= expr . jmp_false expr jf_cf expr COME_FROM
if_exp ::= expr . jmp_false expr jump_absolute_else expr
if_exp ::= expr jmp_false . expr jf_cf expr COME_FROM
if_exp ::= expr jmp_false . expr jump_absolute_else expr
if_exp ::= expr jmp_false expr . jf_cf expr COME_FROM
if_exp ::= expr jmp_false expr . jump_absolute_else expr
if_exp37 ::= expr . expr jf_cfs expr COME_FROM
if_exp37 ::= expr expr . jf_cfs expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false . expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false expr . POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false expr . return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not ::= expr jmp_true . expr jump_forward_else expr COME_FROM
if_exp_not ::= expr jmp_true expr . jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not_lambda ::= expr jmp_true . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not_lambda ::= expr jmp_true expr . return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_ret ::= expr . POP_JUMP_IF_FALSE expr RETURN_END_IF COME_FROM return_expr_or_cond
if_exp_true ::= expr . JUMP_FORWARD expr COME_FROM
ifelsestmt ::= testexpr . c_stmts come_froms else_suite come_froms
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt jf_cfs else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt jf_cfs else_suite opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt jump_forward_else else_suite \e__come_froms
ifelsestmt ::= testexpr . c_stmts_opt jump_forward_else else_suite _come_froms
ifelsestmt ::= testexpr . stmts jf_cfs \e_else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr . stmts jf_cfs \e_else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr . stmts jf_cfs else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr . stmts jf_cfs else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . jf_cfs else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . jf_cfs else_suite opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . jump_forward_else else_suite \e__come_froms
ifelsestmt ::= testexpr \e_c_stmts_opt . jump_forward_else else_suite _come_froms
ifelsestmt ::= testexpr c_stmts . come_froms else_suite come_froms
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jf_cfs else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jf_cfs else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jump_forward_else else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt . jump_forward_else else_suite _come_froms
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt opt_come_from_except
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt jump_absolute_else else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . jump_absolute_else else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt jump_absolute_else . else_suitec
ifelsestmtl ::= testexpr . c_stmts cf_pt else_suite
ifelsestmtl ::= testexpr . c_stmts_opt cf_jf_else else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt cf_jump_back else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt jb_cfs else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt jb_cfs else_suitel JUMP_BACK come_froms
ifelsestmtl ::= testexpr . c_stmts_opt jb_else else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt jump_forward_else else_suitec
ifelsestmtl ::= testexpr \e_c_stmts_opt . cf_jf_else else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . cf_jump_back else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . jb_cfs else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . jb_cfs else_suitel JUMP_BACK come_froms
ifelsestmtl ::= testexpr \e_c_stmts_opt . jb_else else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . jump_forward_else else_suitec
ifelsestmtl ::= testexpr \e_c_stmts_opt jb_cfs . else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt jb_cfs . else_suitel JUMP_BACK come_froms
ifelsestmtl ::= testexpr \e_c_stmts_opt jb_cfs else_suitel . 
ifelsestmtl ::= testexpr \e_c_stmts_opt jb_cfs else_suitel . JUMP_BACK come_froms
ifelsestmtl ::= testexpr \e_c_stmts_opt jb_cfs else_suitel JUMP_BACK . come_froms
ifelsestmtl ::= testexpr \e_c_stmts_opt jb_else . else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt jb_else else_suitel . 
ifelsestmtl ::= testexpr c_stmts . cf_pt else_suite
ifelsestmtl ::= testexpr c_stmts_opt . cf_jf_else else_suitel
ifelsestmtl ::= testexpr c_stmts_opt . cf_jump_back else_suitel
ifelsestmtl ::= testexpr c_stmts_opt . jb_cfs else_suitel
ifelsestmtl ::= testexpr c_stmts_opt . jb_cfs else_suitel JUMP_BACK come_froms
ifelsestmtl ::= testexpr c_stmts_opt . jb_else else_suitel
ifelsestmtl ::= testexpr c_stmts_opt . jump_forward_else else_suitec
ifelsestmtr ::= testexpr . return_if_stmts returns
iflaststmt ::= testexpr . c_stmts
iflaststmt ::= testexpr . c_stmts JUMP_ABSOLUTE
iflaststmt ::= testexpr . c_stmts_opt JUMP_FORWARD
iflaststmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD
iflaststmtl ::= testexpr . c_stmts
iflaststmtl ::= testexpr . c_stmts JUMP_BACK
iflaststmtl ::= testexpr . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexpr . c_stmts JUMP_BACK POP_BLOCK
iflaststmtl ::= testexpr c_stmts . 
iflaststmtl ::= testexpr c_stmts . JUMP_BACK
iflaststmtl ::= testexpr c_stmts . JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexpr c_stmts . JUMP_BACK POP_BLOCK
iflaststmtl ::= testexprl . c_stmts JUMP_BACK
iflaststmtl ::= testexprl . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexprl . c_stmts JUMP_BACK POP_BLOCK
ifpoplaststmtl ::= testexpr . POP_TOP \e_c_stmts_opt
ifpoplaststmtl ::= testexpr . POP_TOP c_stmts_opt
ifstmt ::= testexpr . _ifstmts_jump
ifstmtl ::= testexpr . _ifstmts_jumpl
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jb_cfs ::= \e_come_from_opt JUMP_BACK . come_froms
jb_cfs ::= \e_come_from_opt JUMP_BACK come_froms . 
jb_else ::= JUMP_BACK . COME_FROM
jb_else ::= JUMP_BACK . ELSE
jb_else ::= JUMP_BACK COME_FROM . 
jifop_come_from ::= JUMP_IF_FALSE_OR_POP . come_froms
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
joined_str ::= expr . expr BUILD_STRING_2
joined_str ::= expr . expr expr BUILD_STRING_3
joined_str ::= expr . expr expr expr BUILD_STRING_4
joined_str ::= expr . expr expr expr expr expr expr expr expr BUILD_STRING_9
joined_str ::= expr expr . BUILD_STRING_2
joined_str ::= expr expr . expr BUILD_STRING_3
joined_str ::= expr expr . expr expr BUILD_STRING_4
joined_str ::= expr expr . expr expr expr expr expr expr expr BUILD_STRING_9
joined_str ::= expr expr expr . BUILD_STRING_3
joined_str ::= expr expr expr . expr BUILD_STRING_4
joined_str ::= expr expr expr . expr expr expr expr expr expr BUILD_STRING_9
jump_absolute_else ::= come_froms . _jump COME_FROM
jump_absolute_else ::= jb_else . 
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= _stmts lastl_stmt . 
l_stmts ::= l_stmts . lstmt
l_stmts ::= l_stmts lstmt . 
l_stmts ::= lastl_stmt . 
l_stmts ::= lastl_stmt . come_froms l_stmts
l_stmts ::= lstmt . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lastl_stmt ::= ifelsestmtl . 
list ::= expr . expr BUILD_LIST_2
list ::= expr . expr expr BUILD_LIST_3
list ::= expr . expr expr expr expr expr expr expr expr BUILD_LIST_9
list ::= expr expr . BUILD_LIST_2
list ::= expr expr . expr BUILD_LIST_3
list ::= expr expr . expr expr expr expr expr expr expr BUILD_LIST_9
list ::= expr expr expr . BUILD_LIST_3
list ::= expr expr expr . expr expr expr expr expr expr BUILD_LIST_9
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
named_expr ::= expr . DUP_TOP store
or ::= and . jitop_come_from_expr COME_FROM
or ::= expr_jt . expr
or ::= expr_jt . expr COME_FROM
or ::= expr_jt expr . 
or ::= expr_jt expr . COME_FROM
or ::= expr_pjit . expr POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr . POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr POP_JUMP_IF_FALSE . COME_FROM
pop_ex_return ::= return_expr . ROT_FOUR POP_EXCEPT RETURN_VALUE
popb_return ::= return_expr . POP_BLOCK RETURN_VALUE
pos_arg ::= expr . 
raise_stmt1 ::= expr . RAISE_VARARGS_1
raise_stmt2 ::= expr . expr RAISE_VARARGS_2
raise_stmt2 ::= expr expr . RAISE_VARARGS_2
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_and ::= expr JUMP_IF_FALSE_OR_POP . return_expr_or_cond COME_FROM
ret_and ::= expr JUMP_IF_FALSE_OR_POP return_expr_or_cond . COME_FROM
ret_and ::= expr JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM . 
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return ::= return_expr . discard_tops RETURN_VALUE
return_expr ::= expr . 
return_expr ::= ret_and . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_expr_or_cond ::= return_expr . 
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr . RETURN_END_IF POP_BLOCK
return_if_stmts ::= _stmts . return_if_stmt \e__come_froms
return_if_stmts ::= _stmts . return_if_stmt _come_froms
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
set ::= expr . expr expr BUILD_SET_3
set ::= expr expr . expr BUILD_SET_3
set ::= expr expr expr . BUILD_SET_3
slice2 ::= expr . expr BUILD_SLICE_2
slice2 ::= expr expr . BUILD_SLICE_2
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= call_stmt . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store ::= store_subscript . 
store ::= unpack . 
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
store_subscript ::= expr expr STORE_SUBSCR . 
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript ::= expr expr BINARY_SUBSCR . 
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
testexpr ::= testfalse . 
testexpr ::= testtrue . 
testexpr_cf ::= testexpr . come_froms
testexprl ::= testfalsel . 
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse ::= or . jmp_false COME_FROM
testfalse ::= or jmp_false . COME_FROM
testfalse_not_and ::= and . jmp_true come_froms
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr . jmp_false COME_FROM
testfalsel ::= expr . jmp_true
testfalsel ::= expr jmp_true . 
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr expr . BUILD_TUPLE_2
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
unpack ::= UNPACK_SEQUENCE_2 . store store
unpack ::= UNPACK_SEQUENCE_2 store . store
unpack ::= UNPACK_SEQUENCE_2 store store . 
while1stmt ::= \e__come_froms . l_stmts COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= \e__come_froms l_stmts . COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= _come_froms . l_stmts COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= _come_froms l_stmts . COME_FROM JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= \e__come_froms . l_stmts JUMP_BACK POP_BLOCK
whileTruestmt ::= \e__come_froms l_stmts . JUMP_BACK POP_BLOCK
whileTruestmt ::= \e__come_froms l_stmts JUMP_BACK . POP_BLOCK
whileTruestmt ::= _come_froms . l_stmts JUMP_BACK POP_BLOCK
whileTruestmt ::= _come_froms l_stmts . JUMP_BACK POP_BLOCK
whileTruestmt ::= _come_froms l_stmts JUMP_BACK . POP_BLOCK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= \e__come_froms . pass JUMP_BACK
whileTruestmt38 ::= \e__come_froms \e_pass . JUMP_BACK
whileTruestmt38 ::= \e__come_froms \e_pass JUMP_BACK . 
whileTruestmt38 ::= \e__come_froms l_stmts . JUMP_BACK
whileTruestmt38 ::= \e__come_froms l_stmts . JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= \e__come_froms l_stmts JUMP_BACK . 
whileTruestmt38 ::= \e__come_froms l_stmts JUMP_BACK . COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= _come_froms . l_stmts JUMP_BACK
whileTruestmt38 ::= _come_froms . l_stmts JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= _come_froms . pass JUMP_BACK
whileTruestmt38 ::= _come_froms \e_pass . JUMP_BACK
whileTruestmt38 ::= _come_froms l_stmts . JUMP_BACK
whileTruestmt38 ::= _come_froms l_stmts . JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= _come_froms l_stmts JUMP_BACK . 
whileTruestmt38 ::= _come_froms l_stmts JUMP_BACK . COME_FROM_EXCEPT_CLAUSE
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts JUMP_BACK
whilestmt38 ::= \e__come_froms . testexpr l_stmts come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr returns POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr . l_stmts JUMP_BACK
whilestmt38 ::= \e__come_froms testexpr . l_stmts come_froms
whilestmt38 ::= \e__come_froms testexpr . l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr . l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr . l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms testexpr . returns POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr \e_l_stmts_opt . COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr \e_l_stmts_opt . JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr \e_l_stmts_opt . JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms testexpr \e_l_stmts_opt JUMP_BACK . POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr \e_l_stmts_opt JUMP_BACK . come_froms
whilestmt38 ::= \e__come_froms testexpr \e_l_stmts_opt JUMP_BACK come_froms . 
whilestmt38 ::= \e__come_froms testexpr l_stmts . JUMP_BACK
whilestmt38 ::= \e__come_froms testexpr l_stmts . come_froms
whilestmt38 ::= \e__come_froms testexpr l_stmts JUMP_BACK . 
whilestmt38 ::= \e__come_froms testexpr l_stmts_opt . COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr l_stmts_opt . JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr l_stmts_opt . JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms testexpr l_stmts_opt JUMP_BACK . POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr l_stmts_opt JUMP_BACK . come_froms
whilestmt38 ::= _come_froms . testexpr \e_l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= _come_froms . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= _come_froms . testexpr \e_l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= _come_froms . testexpr l_stmts JUMP_BACK
whilestmt38 ::= _come_froms . testexpr l_stmts come_froms
whilestmt38 ::= _come_froms . testexpr l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= _come_froms . testexpr l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= _come_froms . testexpr l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= _come_froms . testexpr returns POP_BLOCK
whilestmt38 ::= _come_froms testexpr . l_stmts JUMP_BACK
whilestmt38 ::= _come_froms testexpr . l_stmts come_froms
whilestmt38 ::= _come_froms testexpr . l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= _come_froms testexpr . l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= _come_froms testexpr . l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= _come_froms testexpr . returns POP_BLOCK
whilestmt38 ::= _come_froms testexpr \e_l_stmts_opt . COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= _come_froms testexpr \e_l_stmts_opt . JUMP_BACK POP_BLOCK
whilestmt38 ::= _come_froms testexpr \e_l_stmts_opt . JUMP_BACK come_froms
whilestmt38 ::= _come_froms testexpr \e_l_stmts_opt JUMP_BACK . POP_BLOCK
whilestmt38 ::= _come_froms testexpr \e_l_stmts_opt JUMP_BACK . come_froms
whilestmt38 ::= _come_froms testexpr \e_l_stmts_opt JUMP_BACK come_froms . 
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
->               0_0  COLLECTION_START      2  'CONST_DICT'

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_stmts ::= _stmts . stmt
_stmts ::= stmt . 
and ::= expr . JUMP_IF_FALSE_OR_POP expr \e_come_from_opt
and ::= expr . JUMP_IF_FALSE_OR_POP expr come_from_opt
and ::= expr . jifop_come_from expr
and ::= expr . jmp_false expr
and ::= expr . jmp_false expr COME_FROM
and ::= expr . jmp_false expr jmp_false
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign ::= expr store . 
assign2 ::= expr . expr ROT_TWO store store
assign2 ::= expr expr . ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr . expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr expr . ROT_THREE ROT_TWO store store store
async_for_stmt38 ::= expr . async_for store for_block COME_FROM_FINALLY END_ASYNC_FOR
async_forelse_stmt38 ::= expr . GET_AITER SETUP_FINALLY GET_ANEXT LOAD_CONST YIELD_FROM POP_BLOCK store for_block COME_FROM_FINALLY END_ASYNC_FOR else_suite
attribute ::= expr . LOAD_ATTR
attribute37 ::= expr . LOAD_METHOD
attribute37 ::= expr LOAD_METHOD . 
aug_assign1 ::= expr . expr inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr . expr inplace_op store
aug_assign1 ::= expr expr . inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr . inplace_op store
aug_assign2 ::= expr . DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
bin_op ::= expr expr . binary_operator
break ::= POP_BLOCK . BREAK_LOOP
break ::= POP_BLOCK . POP_TOP BREAK_LOOP
call ::= expr . CALL_METHOD_0
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg CALL_METHOD_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg CALL_METHOD_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_METHOD_4
call ::= expr CALL_METHOD_0 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . CALL_METHOD_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg CALL_METHOD_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_METHOD_4
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . CALL_METHOD_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_METHOD_4
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg . pos_arg CALL_METHOD_4
call ::= expr pos_arg pos_arg pos_arg pos_arg . CALL_METHOD_4
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_3 . 
call_kw36 ::= expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_stmt ::= call . 
call_stmt ::= expr . POP_TOP
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
come_from_loops ::= \e_come_from_loops . COME_FROM_LOOP
compare_chained ::= expr . compared_chained_middle ROT_TWO POP_TOP \e__come_froms
compare_chained ::= expr . compared_chained_middle ROT_TWO POP_TOP _come_froms
compare_chained37 ::= expr . compared_chained_middlea_37
compare_chained37 ::= expr . compared_chained_middlec_37
compare_chained37_false ::= expr . compare_chained_right_false_37
compare_chained37_false ::= expr . compared_chained_middle_false_37
compare_chained37_false ::= expr . compared_chained_middleb_false_37
compare_chained_right_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_righta_false_37 POP_TOP JUMP_BACK COME_FROM
compare_single ::= expr . expr COMPARE_OP
compare_single ::= expr expr . COMPARE_OP
compared_chained_middle ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained_right COME_FROM
compared_chained_middle ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compared_chained_middle COME_FROM
compared_chained_middle_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_rightb_false_37 POP_TOP _jump COME_FROM
compared_chained_middle_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_rightc_37 POP_TOP JUMP_FORWARD COME_FROM
compared_chained_middlea_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE
compared_chained_middlea_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_righta_37 COME_FROM POP_TOP COME_FROM
compared_chained_middleb_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_rightb_false_37 POP_TOP _jump COME_FROM
compared_chained_middlec_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_righta_37 POP_TOP
continues ::= _stmts . lastl_stmt continue
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_2
except_ret38 ::= SETUP_FINALLY . expr ROT_FOUR POP_BLOCK POP_EXCEPT CALL_FINALLY RETURN_VALUE COME_FROM COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
except_ret38 ::= SETUP_FINALLY . expr ROT_FOUR POP_BLOCK POP_EXCEPT CALL_FINALLY RETURN_VALUE COME_FROM COME_FROM_FINALLY suite_stmts_opt END_FINALLY
except_ret38 ::= SETUP_FINALLY expr . ROT_FOUR POP_BLOCK POP_EXCEPT CALL_FINALLY RETURN_VALUE COME_FROM COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
except_ret38 ::= SETUP_FINALLY expr . ROT_FOUR POP_BLOCK POP_EXCEPT CALL_FINALLY RETURN_VALUE COME_FROM COME_FROM_FINALLY suite_stmts_opt END_FINALLY
except_return_value ::= expr . POP_BLOCK RETURN_VALUE
except_return_value ::= expr POP_BLOCK . RETURN_VALUE
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= call_kw36 . 
expr ::= get_iter . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_stmt ::= expr . POP_TOP
for38 ::= expr . get_for_iter store for_block
for38 ::= expr . get_for_iter store for_block JUMP_BACK
for38 ::= expr . get_for_iter store for_block JUMP_BACK POP_BLOCK
for38 ::= expr . get_iter store for_block JUMP_BACK
for38 ::= expr get_for_iter . store for_block
for38 ::= expr get_for_iter . store for_block JUMP_BACK
for38 ::= expr get_for_iter . store for_block JUMP_BACK POP_BLOCK
for38 ::= expr get_for_iter store . for_block
for38 ::= expr get_for_iter store . for_block JUMP_BACK
for38 ::= expr get_for_iter store . for_block JUMP_BACK POP_BLOCK
for_block ::= \e__come_froms . l_stmts_opt _come_from_loops JUMP_BACK
for_block ::= \e__come_froms \e_l_stmts_opt . _come_from_loops JUMP_BACK
for_block ::= \e_l_stmts_opt . _come_froms JUMP_BACK
for_block ::= \e_l_stmts_opt . come_from_loops JUMP_BACK
for_block ::= \e_l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= \e_l_stmts_opt \e_come_from_loops . JUMP_BACK
forelselaststmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitec
forelselaststmt38 ::= expr get_for_iter . store for_block POP_BLOCK else_suitec
forelselaststmt38 ::= expr get_for_iter store . for_block POP_BLOCK else_suitec
forelselaststmtl38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitel
forelselaststmtl38 ::= expr get_for_iter . store for_block POP_BLOCK else_suitel
forelselaststmtl38 ::= expr get_for_iter store . for_block POP_BLOCK else_suitel
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_BACK \e__come_froms else_suite
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_BACK _come_froms else_suite
forelsestmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suite
forelsestmt38 ::= expr get_for_iter . store for_block JUMP_BACK \e__come_froms else_suite
forelsestmt38 ::= expr get_for_iter . store for_block JUMP_BACK _come_froms else_suite
forelsestmt38 ::= expr get_for_iter . store for_block POP_BLOCK else_suite
forelsestmt38 ::= expr get_for_iter store . for_block JUMP_BACK \e__come_froms else_suite
forelsestmt38 ::= expr get_for_iter store . for_block JUMP_BACK _come_froms else_suite
forelsestmt38 ::= expr get_for_iter store . for_block POP_BLOCK else_suite
formatted_value1 ::= expr . FORMAT_VALUE
formatted_value_debug ::= LOAD_STR . formatted_value1 BUILD_STRING_2
formatted_value_debug ::= LOAD_STR . formatted_value1 LOAD_STR BUILD_STRING_3
formatted_value_debug ::= LOAD_STR . formatted_value2 BUILD_STRING_2
formatted_value_debug ::= LOAD_STR . formatted_value2 LOAD_STR BUILD_STRING_3
get_for_iter ::= GET_ITER . _come_froms FOR_ITER
get_for_iter ::= GET_ITER \e__come_froms . FOR_ITER
get_for_iter ::= GET_ITER \e__come_froms FOR_ITER . 
get_iter ::= expr . GET_ITER
get_iter ::= expr GET_ITER . 
if_exp ::= expr . jmp_false expr jf_cf expr COME_FROM
if_exp ::= expr . jmp_false expr jump_absolute_else expr
if_exp37 ::= expr . expr jf_cfs expr COME_FROM
if_exp37 ::= expr expr . jf_cfs expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_true ::= expr . JUMP_FORWARD expr COME_FROM
import ::= LOAD_CONST . LOAD_CONST alias
import_as37 ::= LOAD_CONST . LOAD_CONST importlist37 store POP_TOP
import_from ::= LOAD_CONST . LOAD_CONST IMPORT_NAME importlist POP_TOP
import_from ::= LOAD_CONST . LOAD_CONST importlist POP_TOP
import_from37 ::= LOAD_CONST . LOAD_CONST IMPORT_NAME_ATTR importlist37 POP_TOP
import_from_as37 ::= LOAD_CONST . LOAD_CONST import_from_attr37 store POP_TOP
import_from_star ::= LOAD_CONST . LOAD_CONST IMPORT_NAME IMPORT_STAR
import_from_star ::= LOAD_CONST . LOAD_CONST IMPORT_NAME_ATTR IMPORT_STAR
importmultiple ::= LOAD_CONST . LOAD_CONST alias imports_cont
joined_str ::= expr . expr BUILD_STRING_2
joined_str ::= expr . expr expr BUILD_STRING_3
joined_str ::= expr . expr expr expr BUILD_STRING_4
joined_str ::= expr . expr expr expr expr expr expr expr expr BUILD_STRING_9
joined_str ::= expr expr . BUILD_STRING_2
joined_str ::= expr expr . expr BUILD_STRING_3
joined_str ::= expr expr . expr expr BUILD_STRING_4
joined_str ::= expr expr . expr expr expr expr expr expr expr BUILD_STRING_9
joined_str ::= expr expr expr . BUILD_STRING_3
joined_str ::= expr expr expr . expr BUILD_STRING_4
joined_str ::= expr expr expr . expr expr expr expr expr expr BUILD_STRING_9
joined_str ::= expr expr expr expr . BUILD_STRING_4
joined_str ::= expr expr expr expr . expr expr expr expr expr BUILD_STRING_9
joined_str ::= expr expr expr expr expr . expr expr expr expr BUILD_STRING_9
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= l_stmts . lstmt
l_stmts ::= lstmt . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lc_setup_finally ::= LOAD_CONST . SETUP_FINALLY
list ::= expr . expr BUILD_LIST_2
list ::= expr . expr expr BUILD_LIST_3
list ::= expr . expr expr expr expr expr expr expr expr BUILD_LIST_9
list ::= expr expr . BUILD_LIST_2
list ::= expr expr . expr BUILD_LIST_3
list ::= expr expr . expr expr expr expr expr expr expr BUILD_LIST_9
list ::= expr expr expr . BUILD_LIST_3
list ::= expr expr expr . expr expr expr expr expr expr BUILD_LIST_9
list ::= expr expr expr expr . expr expr expr expr expr BUILD_LIST_9
list ::= expr expr expr expr expr . expr expr expr expr BUILD_LIST_9
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
named_expr ::= expr . DUP_TOP store
pop_ex_return ::= return_expr . ROT_FOUR POP_EXCEPT RETURN_VALUE
popb_return ::= return_expr . POP_BLOCK RETURN_VALUE
popb_return ::= return_expr POP_BLOCK . RETURN_VALUE
pos_arg ::= expr . 
raise_stmt1 ::= expr . RAISE_VARARGS_1
raise_stmt2 ::= expr . expr RAISE_VARARGS_2
raise_stmt2 ::= expr expr . RAISE_VARARGS_2
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return ::= return_expr . discard_tops RETURN_VALUE
return_except ::= stmts . POP_BLOCK return
return_expr ::= expr . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr . RETURN_END_IF POP_BLOCK
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
returns_in_except ::= _stmts . except_return_value
set ::= expr . expr expr BUILD_SET_3
set ::= expr expr . expr BUILD_SET_3
set ::= expr expr expr . BUILD_SET_3
sf_pb_call_returns ::= SETUP_FINALLY . POP_BLOCK CALL_FINALLY returns
slice2 ::= expr . expr BUILD_SLICE_2
slice2 ::= expr expr . BUILD_SLICE_2
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= call_stmt . 
stmt ::= with_as . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
suite_stmts ::= _stmts . 
suite_stmts_opt ::= suite_stmts . 
testfalse ::= expr . jmp_false
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalsel ::= expr . jmp_true
testtrue ::= expr . jmp_true
try_elsestmtl38 ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK except_handler38 COME_FROM else_suitel \e_opt_come_from_except
try_elsestmtl38 ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK except_handler38 COME_FROM else_suitel opt_come_from_except
try_elsestmtl38 ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK except_handler38 COME_FROM else_suitel \e_opt_come_from_except
try_elsestmtl38 ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK except_handler38 COME_FROM else_suitel opt_come_from_except
try_elsestmtl38 ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK except_handler38 COME_FROM else_suitel \e_opt_come_from_except
try_elsestmtl38 ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK except_handler38 COME_FROM else_suitel opt_come_from_except
try_except ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK except_handler38
try_except ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK except_handler38
try_except ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK except_handler38
try_except38 ::= SETUP_FINALLY . POP_BLOCK POP_TOP \e_suite_stmts_opt except_handler38a
try_except38 ::= SETUP_FINALLY . POP_BLOCK POP_TOP suite_stmts_opt except_handler38a
try_except38 ::= SETUP_FINALLY . POP_BLOCK suite_stmts except_handler38b
try_except38r ::= SETUP_FINALLY . return_except except_handler38b
try_except38r2 ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP \e_cond_except_stmts_opt POP_EXCEPT return END_FINALLY COME_FROM
try_except38r2 ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP cond_except_stmts_opt POP_EXCEPT return END_FINALLY COME_FROM
try_except38r2 ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP \e_cond_except_stmts_opt POP_EXCEPT return END_FINALLY COME_FROM
try_except38r2 ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP cond_except_stmts_opt POP_EXCEPT return END_FINALLY COME_FROM
try_except38r2 ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP \e_cond_except_stmts_opt POP_EXCEPT return END_FINALLY COME_FROM
try_except38r2 ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP cond_except_stmts_opt POP_EXCEPT return END_FINALLY COME_FROM
try_except38r3 ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY \e_cond_except_stmts_opt POP_EXCEPT return COME_FROM END_FINALLY COME_FROM
try_except38r3 ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY cond_except_stmts_opt POP_EXCEPT return COME_FROM END_FINALLY COME_FROM
try_except38r3 ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY \e_cond_except_stmts_opt POP_EXCEPT return COME_FROM END_FINALLY COME_FROM
try_except38r3 ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY cond_except_stmts_opt POP_EXCEPT return COME_FROM END_FINALLY COME_FROM
try_except38r3 ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY \e_cond_except_stmts_opt POP_EXCEPT return COME_FROM END_FINALLY COME_FROM
try_except38r3 ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY cond_except_stmts_opt POP_EXCEPT return COME_FROM END_FINALLY COME_FROM
try_except38r4 ::= SETUP_FINALLY . returns_in_except COME_FROM_FINALLY except_cond1 return COME_FROM END_FINALLY
try_except_as ::= SETUP_FINALLY . POP_BLOCK suite_stmts except_handler_as END_FINALLY COME_FROM
try_except_as ::= SETUP_FINALLY . suite_stmts except_handler_as END_FINALLY COME_FROM
try_except_as ::= SETUP_FINALLY suite_stmts . except_handler_as END_FINALLY COME_FROM
try_except_ret38 ::= SETUP_FINALLY . returns except_ret38a
tryfinally36 ::= SETUP_FINALLY . returns COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinally36 ::= SETUP_FINALLY . returns COME_FROM_FINALLY suite_stmts
tryfinally36 ::= SETUP_FINALLY . returns COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinally38astmt ::= LOAD_CONST . SETUP_FINALLY \e_suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY POP_TOP \e_suite_stmts_opt END_FINALLY POP_TOP
tryfinally38astmt ::= LOAD_CONST . SETUP_FINALLY \e_suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY POP_TOP suite_stmts_opt END_FINALLY POP_TOP
tryfinally38astmt ::= LOAD_CONST . SETUP_FINALLY suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY POP_TOP \e_suite_stmts_opt END_FINALLY POP_TOP
tryfinally38astmt ::= LOAD_CONST . SETUP_FINALLY suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY POP_TOP suite_stmts_opt END_FINALLY POP_TOP
tryfinally38rstmt3 ::= SETUP_FINALLY . expr POP_BLOCK CALL_FINALLY RETURN_VALUE COME_FROM COME_FROM_FINALLY ss_end_finally
tryfinally38rstmt3 ::= SETUP_FINALLY expr . POP_BLOCK CALL_FINALLY RETURN_VALUE COME_FROM COME_FROM_FINALLY ss_end_finally
tryfinally38stmt ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY suite_stmts_opt END_FINALLY
tryfinally_return_stmt ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_FINALLY
tryfinally_return_stmt ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_FINALLY
tryfinally_return_stmt ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_FINALLY
tryfinallystmt ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr expr . BUILD_TUPLE_2
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
while1stmt ::= \e__come_froms . l_stmts COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= \e__come_froms l_stmts . COME_FROM JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= \e__come_froms . l_stmts JUMP_BACK POP_BLOCK
whileTruestmt ::= \e__come_froms l_stmts . JUMP_BACK POP_BLOCK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= \e__come_froms . pass JUMP_BACK
whileTruestmt38 ::= \e__come_froms \e_pass . JUMP_BACK
whileTruestmt38 ::= \e__come_froms l_stmts . JUMP_BACK
whileTruestmt38 ::= \e__come_froms l_stmts . JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts JUMP_BACK
whilestmt38 ::= \e__come_froms . testexpr l_stmts come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr returns POP_BLOCK
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP \e_suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP \e_suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with_as ::= expr . SETUP_WITH store \e_suite_stmts_opt COME_FROM_WITH with_suffix
with_as ::= expr . SETUP_WITH store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH
with_as ::= expr . SETUP_WITH store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with_as ::= expr . SETUP_WITH store suite_stmts POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with_as ::= expr . SETUP_WITH store suite_stmts_opt COME_FROM_WITH with_suffix
with_as ::= expr . SETUP_WITH store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH
with_as ::= expr . SETUP_WITH store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with_as ::= expr SETUP_WITH . store \e_suite_stmts_opt COME_FROM_WITH with_suffix
with_as ::= expr SETUP_WITH . store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH
with_as ::= expr SETUP_WITH . store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with_as ::= expr SETUP_WITH . store suite_stmts POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with_as ::= expr SETUP_WITH . store suite_stmts_opt COME_FROM_WITH with_suffix
with_as ::= expr SETUP_WITH . store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH
with_as ::= expr SETUP_WITH . store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with_as ::= expr SETUP_WITH store . suite_stmts POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with_as ::= expr SETUP_WITH store . suite_stmts_opt COME_FROM_WITH with_suffix
with_as ::= expr SETUP_WITH store . suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH
with_as ::= expr SETUP_WITH store . suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with_as ::= expr SETUP_WITH store \e_suite_stmts_opt . COME_FROM_WITH with_suffix
with_as ::= expr SETUP_WITH store \e_suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_WITH
with_as ::= expr SETUP_WITH store \e_suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with_as ::= expr SETUP_WITH store suite_stmts . POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with_as ::= expr SETUP_WITH store suite_stmts POP_BLOCK . BEGIN_FINALLY COME_FROM_WITH with_suffix
with_as ::= expr SETUP_WITH store suite_stmts POP_BLOCK BEGIN_FINALLY . COME_FROM_WITH with_suffix
with_as ::= expr SETUP_WITH store suite_stmts POP_BLOCK BEGIN_FINALLY COME_FROM_WITH . with_suffix
with_as ::= expr SETUP_WITH store suite_stmts POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix . 
with_as ::= expr SETUP_WITH store suite_stmts_opt . COME_FROM_WITH with_suffix
with_as ::= expr SETUP_WITH store suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_WITH
with_as ::= expr SETUP_WITH store suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with_as ::= expr SETUP_WITH store suite_stmts_opt POP_BLOCK . LOAD_CONST COME_FROM_WITH
with_as ::= expr SETUP_WITH store suite_stmts_opt POP_BLOCK . LOAD_CONST COME_FROM_WITH with_suffix
with_as_pass ::= expr . SETUP_WITH store \e_pass POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with_as_pass ::= expr . SETUP_WITH store pass POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with_as_pass ::= expr SETUP_WITH . store \e_pass POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with_as_pass ::= expr SETUP_WITH . store pass POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with_as_pass ::= expr SETUP_WITH store . pass POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with_as_pass ::= expr SETUP_WITH store \e_pass . POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with_suffix ::= WITH_CLEANUP_START . WITH_CLEANUP_FINISH END_FINALLY
with_suffix ::= WITH_CLEANUP_START WITH_CLEANUP_FINISH . END_FINALLY
with_suffix ::= WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY . 
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
-> 
 L. 802         0  LOAD_CONST               ('utf-8', 'utf-8-sig', 'gbk', 'gb18030')
                   2  GET_ITER         
                   4  FOR_ITER             80  'to 80'
                   6  STORE_FAST               'enc'

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_come_froms ::= \e__come_froms COME_FROM . 
_come_froms ::= _come_froms . COME_FROM
_come_froms ::= _come_froms . COME_FROM_LOOP
_come_froms ::= _come_froms COME_FROM . 
_ifstmts_jump ::= COME_FROM . c_stmts come_froms
_ifstmts_jump ::= COME_FROM c_stmts . come_froms
_ifstmts_jump ::= COME_FROM c_stmts come_froms . 
_ifstmts_jump ::= \e_c_stmts_opt . COME_FROM
_ifstmts_jump ::= \e_c_stmts_opt . ELSE
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD \e__come_froms
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD _come_froms
_ifstmts_jump ::= \e_c_stmts_opt . come_froms
_ifstmts_jump ::= \e_c_stmts_opt COME_FROM . 
_ifstmts_jump ::= \e_c_stmts_opt come_froms . 
_ifstmts_jump ::= c_stmts_opt . COME_FROM
_ifstmts_jump ::= c_stmts_opt . ELSE
_ifstmts_jump ::= c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD \e__come_froms
_ifstmts_jump ::= c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD _come_froms
_ifstmts_jump ::= c_stmts_opt . come_froms
_ifstmts_jump ::= c_stmts_opt COME_FROM . 
_ifstmts_jump ::= c_stmts_opt come_froms . 
_ifstmts_jumpl ::= COME_FROM . c_stmts JUMP_BACK
_ifstmts_jumpl ::= COME_FROM . c_stmts JUMP_FORWARD
_ifstmts_jumpl ::= COME_FROM c_stmts . JUMP_BACK
_ifstmts_jumpl ::= COME_FROM c_stmts . JUMP_FORWARD
_ifstmts_jumpl ::= _ifstmts_jump . 
_ifstmts_jumpl ::= c_stmts . JUMP_BACK
_stmts ::= _stmts . stmt
_stmts ::= _stmts stmt . 
_stmts ::= stmt . 
and ::= expr . JUMP_IF_FALSE_OR_POP expr \e_come_from_opt
and ::= expr . JUMP_IF_FALSE_OR_POP expr come_from_opt
and ::= expr . jifop_come_from expr
and ::= expr . jmp_false expr
and ::= expr . jmp_false expr COME_FROM
and ::= expr . jmp_false expr jmp_false
and ::= expr JUMP_IF_FALSE_OR_POP . expr \e_come_from_opt
and ::= expr JUMP_IF_FALSE_OR_POP . expr come_from_opt
and ::= expr JUMP_IF_FALSE_OR_POP expr . come_from_opt
and ::= expr JUMP_IF_FALSE_OR_POP expr \e_come_from_opt . 
and ::= expr JUMP_IF_FALSE_OR_POP expr come_from_opt . 
and ::= expr jmp_false . expr
and ::= expr jmp_false . expr COME_FROM
and ::= expr jmp_false . expr jmp_false
and ::= expr jmp_false expr . 
and ::= expr jmp_false expr . COME_FROM
and ::= expr jmp_false expr . jmp_false
and ::= expr jmp_false expr COME_FROM . 
and ::= expr jmp_false expr jmp_false . 
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false . expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false expr . POP_JUMP_IF_TRUE
and_not ::= expr jmp_false expr POP_JUMP_IF_TRUE . 
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true . LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert_invert ::= testtrue . LOAD_GLOBAL RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign ::= expr store . 
assign2 ::= expr . expr ROT_TWO store store
assign2 ::= expr expr . ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr . expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr expr . ROT_THREE ROT_TWO store store store
async_for_stmt38 ::= expr . async_for store for_block COME_FROM_FINALLY END_ASYNC_FOR
async_forelse_stmt38 ::= expr . GET_AITER SETUP_FINALLY GET_ANEXT LOAD_CONST YIELD_FROM POP_BLOCK store for_block COME_FROM_FINALLY END_ASYNC_FOR else_suite
attribute ::= expr . LOAD_ATTR
attribute ::= expr LOAD_ATTR . 
attribute37 ::= expr . LOAD_METHOD
attribute37 ::= expr LOAD_METHOD . 
aug_assign1 ::= expr . expr inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr . expr inplace_op store
aug_assign1 ::= expr expr . inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr . inplace_op store
aug_assign2 ::= expr . DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
bin_op ::= expr expr . binary_operator
bin_op ::= expr expr binary_operator . 
binary_operator ::= BINARY_ADD . 
break ::= POP_TOP . BREAK_LOOP
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= _stmts lastc_stmt . 
c_stmts ::= lastc_stmt . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg CALL_METHOD_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg CALL_METHOD_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr . pos_arg pos_arg pos_arg CALL_METHOD_3
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_METHOD_4
call ::= expr CALL_FUNCTION_0 . 
call ::= expr CALL_METHOD_0 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . CALL_METHOD_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg CALL_METHOD_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg CALL_METHOD_3
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_METHOD_4
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg CALL_METHOD_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . CALL_METHOD_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg CALL_METHOD_3
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_METHOD_4
call ::= expr pos_arg pos_arg CALL_FUNCTION_2 . 
call ::= expr pos_arg pos_arg CALL_METHOD_2 . 
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg . CALL_METHOD_3
call ::= expr pos_arg pos_arg pos_arg . pos_arg CALL_METHOD_4
call ::= expr pos_arg pos_arg pos_arg CALL_FUNCTION_3 . 
call ::= expr pos_arg pos_arg pos_arg pos_arg . CALL_METHOD_4
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4 . 
call_kw36 ::= expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_7
call_stmt ::= call . 
call_stmt ::= expr . POP_TOP
call_stmt ::= expr POP_TOP . 
cf_jf_else ::= come_froms . JUMP_FORWARD ELSE
cf_jump_back ::= COME_FROM . JUMP_BACK
cf_pt ::= COME_FROM . POP_TOP
cf_pt ::= COME_FROM POP_TOP . 
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
come_from_loops ::= \e_come_from_loops . COME_FROM_LOOP
come_from_opt ::= COME_FROM . 
come_froms ::= COME_FROM . 
come_froms ::= come_froms . COME_FROM
come_froms ::= come_froms COME_FROM . 
compare ::= compare_single . 
compare_chained ::= expr . compared_chained_middle ROT_TWO POP_TOP \e__come_froms
compare_chained ::= expr . compared_chained_middle ROT_TWO POP_TOP _come_froms
compare_chained37 ::= expr . compared_chained_middlea_37
compare_chained37 ::= expr . compared_chained_middlec_37
compare_chained37_false ::= expr . compare_chained_right_false_37
compare_chained37_false ::= expr . compared_chained_middle_false_37
compare_chained37_false ::= expr . compared_chained_middleb_false_37
compare_chained_right_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_righta_false_37 POP_TOP JUMP_BACK COME_FROM
compare_single ::= expr . expr COMPARE_OP
compare_single ::= expr expr . COMPARE_OP
compare_single ::= expr expr COMPARE_OP . 
compared_chained_middle ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained_right COME_FROM
compared_chained_middle ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compared_chained_middle COME_FROM
compared_chained_middle_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_rightb_false_37 POP_TOP _jump COME_FROM
compared_chained_middle_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_rightc_37 POP_TOP JUMP_FORWARD COME_FROM
compared_chained_middlea_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE
compared_chained_middlea_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_righta_37 COME_FROM POP_TOP COME_FROM
compared_chained_middleb_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_rightb_false_37 POP_TOP _jump COME_FROM
compared_chained_middlec_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_righta_37 POP_TOP
continues ::= _stmts . lastl_stmt continue
continues ::= _stmts lastl_stmt . continue
continues ::= lastl_stmt . continue
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr . expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_2
dict ::= expr expr expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr expr expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr expr expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr expr expr expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_5
else_suite ::= suite_stmts . 
else_suite_opt ::= else_suite . 
else_suitec ::= c_stmts . 
else_suitel ::= l_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= and . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= bin_op . 
expr ::= call . 
expr ::= call_kw36 . 
expr ::= compare . 
expr ::= formatted_value1 . 
expr ::= formatted_value_debug . 
expr ::= get_iter . 
expr ::= if_exp . 
expr ::= joined_str . 
expr ::= or . 
expr ::= slice2 . 
expr ::= subscript . 
expr ::= unary_not . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_jt ::= expr jmp_true . 
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit ::= expr POP_JUMP_IF_TRUE . 
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_pjit_come_from ::= expr POP_JUMP_IF_TRUE . COME_FROM
expr_stmt ::= expr . POP_TOP
expr_stmt ::= expr POP_TOP . 
for38 ::= expr . get_for_iter store for_block
for38 ::= expr . get_for_iter store for_block JUMP_BACK
for38 ::= expr . get_for_iter store for_block JUMP_BACK POP_BLOCK
for38 ::= expr . get_iter store for_block JUMP_BACK
for38 ::= expr get_for_iter . store for_block
for38 ::= expr get_for_iter . store for_block JUMP_BACK
for38 ::= expr get_for_iter . store for_block JUMP_BACK POP_BLOCK
for38 ::= expr get_for_iter store . for_block
for38 ::= expr get_for_iter store . for_block JUMP_BACK
for38 ::= expr get_for_iter store . for_block JUMP_BACK POP_BLOCK
for38 ::= expr get_for_iter store for_block . 
for38 ::= expr get_for_iter store for_block . JUMP_BACK
for38 ::= expr get_for_iter store for_block . JUMP_BACK POP_BLOCK
for_block ::= \e__come_froms . l_stmts_opt _come_from_loops JUMP_BACK
for_block ::= \e__come_froms \e_l_stmts_opt . _come_from_loops JUMP_BACK
for_block ::= \e__come_froms l_stmts_opt . _come_from_loops JUMP_BACK
for_block ::= \e_l_stmts_opt . _come_froms JUMP_BACK
for_block ::= \e_l_stmts_opt . come_from_loops JUMP_BACK
for_block ::= \e_l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= \e_l_stmts_opt \e_come_from_loops . JUMP_BACK
for_block ::= l_stmts . 
for_block ::= l_stmts . JUMP_BACK
for_block ::= l_stmts_opt . _come_froms JUMP_BACK
for_block ::= l_stmts_opt . come_from_loops JUMP_BACK
for_block ::= l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= l_stmts_opt \e_come_from_loops . JUMP_BACK
for_block ::= l_stmts_opt _come_froms . JUMP_BACK
forelselaststmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitec
forelselaststmt38 ::= expr get_for_iter . store for_block POP_BLOCK else_suitec
forelselaststmt38 ::= expr get_for_iter store . for_block POP_BLOCK else_suitec
forelselaststmt38 ::= expr get_for_iter store for_block . POP_BLOCK else_suitec
forelselaststmtl38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitel
forelselaststmtl38 ::= expr get_for_iter . store for_block POP_BLOCK else_suitel
forelselaststmtl38 ::= expr get_for_iter store . for_block POP_BLOCK else_suitel
forelselaststmtl38 ::= expr get_for_iter store for_block . POP_BLOCK else_suitel
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_BACK \e__come_froms else_suite
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_BACK _come_froms else_suite
forelsestmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suite
forelsestmt38 ::= expr get_for_iter . store for_block JUMP_BACK \e__come_froms else_suite
forelsestmt38 ::= expr get_for_iter . store for_block JUMP_BACK _come_froms else_suite
forelsestmt38 ::= expr get_for_iter . store for_block POP_BLOCK else_suite
forelsestmt38 ::= expr get_for_iter store . for_block JUMP_BACK \e__come_froms else_suite
forelsestmt38 ::= expr get_for_iter store . for_block JUMP_BACK _come_froms else_suite
forelsestmt38 ::= expr get_for_iter store . for_block POP_BLOCK else_suite
forelsestmt38 ::= expr get_for_iter store for_block . JUMP_BACK \e__come_froms else_suite
forelsestmt38 ::= expr get_for_iter store for_block . JUMP_BACK _come_froms else_suite
forelsestmt38 ::= expr get_for_iter store for_block . POP_BLOCK else_suite
formatted_value1 ::= expr . FORMAT_VALUE
formatted_value1 ::= expr FORMAT_VALUE . 
formatted_value_debug ::= LOAD_STR . formatted_value1 BUILD_STRING_2
formatted_value_debug ::= LOAD_STR . formatted_value1 LOAD_STR BUILD_STRING_3
formatted_value_debug ::= LOAD_STR . formatted_value2 BUILD_STRING_2
formatted_value_debug ::= LOAD_STR . formatted_value2 LOAD_STR BUILD_STRING_3
formatted_value_debug ::= LOAD_STR formatted_value1 . BUILD_STRING_2
formatted_value_debug ::= LOAD_STR formatted_value1 . LOAD_STR BUILD_STRING_3
formatted_value_debug ::= LOAD_STR formatted_value1 LOAD_STR . BUILD_STRING_3
formatted_value_debug ::= LOAD_STR formatted_value1 LOAD_STR BUILD_STRING_3 . 
get_for_iter ::= GET_ITER . _come_froms FOR_ITER
get_for_iter ::= GET_ITER \e__come_froms . FOR_ITER
get_for_iter ::= GET_ITER \e__come_froms FOR_ITER . 
get_for_iter ::= GET_ITER _come_froms . FOR_ITER
get_for_iter ::= GET_ITER _come_froms FOR_ITER . 
get_iter ::= expr . GET_ITER
get_iter ::= expr GET_ITER . 
if_exp ::= expr . jmp_false expr jf_cf expr COME_FROM
if_exp ::= expr . jmp_false expr jump_absolute_else expr
if_exp ::= expr jmp_false . expr jf_cf expr COME_FROM
if_exp ::= expr jmp_false . expr jump_absolute_else expr
if_exp ::= expr jmp_false expr . jf_cf expr COME_FROM
if_exp ::= expr jmp_false expr . jump_absolute_else expr
if_exp ::= expr jmp_false expr jf_cf . expr COME_FROM
if_exp ::= expr jmp_false expr jf_cf expr . COME_FROM
if_exp ::= expr jmp_false expr jf_cf expr COME_FROM . 
if_exp37 ::= expr . expr jf_cfs expr COME_FROM
if_exp37 ::= expr expr . jf_cfs expr COME_FROM
if_exp_37a ::= and_not . expr JUMP_FORWARD come_froms expr COME_FROM
if_exp_37a ::= and_not expr . JUMP_FORWARD come_froms expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false . expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false expr . POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false expr POP_JUMP_IF_FALSE . jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false expr . return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not ::= expr jmp_true . expr jump_forward_else expr COME_FROM
if_exp_not ::= expr jmp_true expr . jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not_lambda ::= expr jmp_true . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not_lambda ::= expr jmp_true expr . return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_ret ::= expr . POP_JUMP_IF_FALSE expr RETURN_END_IF COME_FROM return_expr_or_cond
if_exp_true ::= expr . JUMP_FORWARD expr COME_FROM
if_exp_true ::= expr JUMP_FORWARD . expr COME_FROM
ifelsestmt ::= testexpr . c_stmts come_froms else_suite come_froms
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt jf_cfs else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt jf_cfs else_suite opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt jump_forward_else else_suite \e__come_froms
ifelsestmt ::= testexpr . c_stmts_opt jump_forward_else else_suite _come_froms
ifelsestmt ::= testexpr . stmts jf_cfs \e_else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr . stmts jf_cfs \e_else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr . stmts jf_cfs else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr . stmts jf_cfs else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . jf_cfs else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . jf_cfs else_suite opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . jump_forward_else else_suite \e__come_froms
ifelsestmt ::= testexpr \e_c_stmts_opt . jump_forward_else else_suite _come_froms
ifelsestmt ::= testexpr c_stmts . come_froms else_suite come_froms
ifelsestmt ::= testexpr c_stmts come_froms . else_suite come_froms
ifelsestmt ::= testexpr c_stmts come_froms else_suite . come_froms
ifelsestmt ::= testexpr c_stmts come_froms else_suite come_froms . 
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jf_cfs else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jf_cfs else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jump_forward_else else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt . jump_forward_else else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs . else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs . else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs else_suite . opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs else_suite \e_opt_come_from_except . 
ifelsestmt ::= testexpr c_stmts_opt jf_cfs else_suite opt_come_from_except . 
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else . else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else . else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else else_suite . _come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else else_suite \e__come_froms . 
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else else_suite _come_froms . 
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs . else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs . else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt . opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt \e_opt_come_from_except . 
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt opt_come_from_except . 
ifelsestmt ::= testexpr stmts jf_cfs else_suite_opt . opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs else_suite_opt \e_opt_come_from_except . 
ifelsestmt ::= testexpr stmts jf_cfs else_suite_opt opt_come_from_except . 
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt jump_absolute_else else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . jump_absolute_else else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt jump_absolute_else . else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . jump_absolute_else else_suitec
ifelsestmtl ::= testexpr . c_stmts cf_pt else_suite
ifelsestmtl ::= testexpr . c_stmts_opt cf_jf_else else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt cf_jump_back else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt jb_cfs else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt jb_cfs else_suitel JUMP_BACK come_froms
ifelsestmtl ::= testexpr . c_stmts_opt jb_else else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt jump_forward_else else_suitec
ifelsestmtl ::= testexpr \e_c_stmts_opt . cf_jf_else else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . cf_jump_back else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . jb_cfs else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . jb_cfs else_suitel JUMP_BACK come_froms
ifelsestmtl ::= testexpr \e_c_stmts_opt . jb_else else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . jump_forward_else else_suitec
ifelsestmtl ::= testexpr \e_c_stmts_opt jb_cfs . else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt jb_cfs . else_suitel JUMP_BACK come_froms
ifelsestmtl ::= testexpr \e_c_stmts_opt jb_cfs else_suitel . 
ifelsestmtl ::= testexpr \e_c_stmts_opt jb_cfs else_suitel . JUMP_BACK come_froms
ifelsestmtl ::= testexpr \e_c_stmts_opt jb_else . else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt jb_else else_suitel . 
ifelsestmtl ::= testexpr c_stmts . cf_pt else_suite
ifelsestmtl ::= testexpr c_stmts cf_pt . else_suite
ifelsestmtl ::= testexpr c_stmts_opt . cf_jf_else else_suitel
ifelsestmtl ::= testexpr c_stmts_opt . cf_jump_back else_suitel
ifelsestmtl ::= testexpr c_stmts_opt . jb_cfs else_suitel
ifelsestmtl ::= testexpr c_stmts_opt . jb_cfs else_suitel JUMP_BACK come_froms
ifelsestmtl ::= testexpr c_stmts_opt . jb_else else_suitel
ifelsestmtl ::= testexpr c_stmts_opt . jump_forward_else else_suitec
ifelsestmtl ::= testexpr c_stmts_opt jump_forward_else . else_suitec
ifelsestmtl ::= testexpr c_stmts_opt jump_forward_else else_suitec . 
ifelsestmtl ::= testexpr_cf . c_stmts_opt jb_else else_suitel
ifelsestmtl ::= testexpr_cf \e_c_stmts_opt . jb_else else_suitel
ifelsestmtl ::= testexpr_cf c_stmts_opt . jb_else else_suitel
ifelsestmtr ::= testexpr . return_if_stmts returns
iflaststmt ::= testexpr . c_stmts
iflaststmt ::= testexpr . c_stmts JUMP_ABSOLUTE
iflaststmt ::= testexpr . c_stmts_opt JUMP_FORWARD
iflaststmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD
iflaststmt ::= testexpr c_stmts . 
iflaststmt ::= testexpr c_stmts . JUMP_ABSOLUTE
iflaststmt ::= testexpr c_stmts_opt . JUMP_FORWARD
iflaststmtl ::= testexpr . c_stmts
iflaststmtl ::= testexpr . c_stmts JUMP_BACK
iflaststmtl ::= testexpr . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexpr . c_stmts JUMP_BACK POP_BLOCK
iflaststmtl ::= testexpr c_stmts . 
iflaststmtl ::= testexpr c_stmts . JUMP_BACK
iflaststmtl ::= testexpr c_stmts . JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexpr c_stmts . JUMP_BACK POP_BLOCK
iflaststmtl ::= testexprl . c_stmts JUMP_BACK
iflaststmtl ::= testexprl . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexprl . c_stmts JUMP_BACK POP_BLOCK
iflaststmtl ::= testexprl c_stmts . JUMP_BACK
iflaststmtl ::= testexprl c_stmts . JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexprl c_stmts . JUMP_BACK POP_BLOCK
ifpoplaststmtl ::= testexpr . POP_TOP \e_c_stmts_opt
ifpoplaststmtl ::= testexpr . POP_TOP c_stmts_opt
ifpoplaststmtl ::= testexpr POP_TOP . c_stmts_opt
ifpoplaststmtl ::= testexpr POP_TOP \e_c_stmts_opt . 
ifstmt ::= testexpr . _ifstmts_jump
ifstmt ::= testexpr _ifstmts_jump . 
ifstmtl ::= testexpr . _ifstmts_jumpl
ifstmtl ::= testexpr _ifstmts_jumpl . 
import ::= LOAD_CONST . LOAD_CONST alias
import_as37 ::= LOAD_CONST . LOAD_CONST importlist37 store POP_TOP
import_from ::= LOAD_CONST . LOAD_CONST IMPORT_NAME importlist POP_TOP
import_from ::= LOAD_CONST . LOAD_CONST importlist POP_TOP
import_from37 ::= LOAD_CONST . LOAD_CONST IMPORT_NAME_ATTR importlist37 POP_TOP
import_from_as37 ::= LOAD_CONST . LOAD_CONST import_from_attr37 store POP_TOP
import_from_star ::= LOAD_CONST . LOAD_CONST IMPORT_NAME IMPORT_STAR
import_from_star ::= LOAD_CONST . LOAD_CONST IMPORT_NAME_ATTR IMPORT_STAR
importmultiple ::= LOAD_CONST . LOAD_CONST alias imports_cont
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jb_cfs ::= \e_come_from_opt JUMP_BACK . come_froms
jb_cfs ::= \e_come_from_opt JUMP_BACK come_froms . 
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
jb_else ::= JUMP_BACK . COME_FROM
jb_else ::= JUMP_BACK . ELSE
jb_else ::= JUMP_BACK COME_FROM . 
jf_cf ::= JUMP_FORWARD . COME_FROM
jf_cf ::= JUMP_FORWARD COME_FROM . 
jf_cfs ::= JUMP_FORWARD . _come_froms
jf_cfs ::= JUMP_FORWARD \e__come_froms . 
jf_cfs ::= JUMP_FORWARD _come_froms . 
jifop_come_from ::= JUMP_IF_FALSE_OR_POP . come_froms
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
joined_str ::= expr . expr BUILD_STRING_2
joined_str ::= expr . expr expr BUILD_STRING_3
joined_str ::= expr . expr expr expr BUILD_STRING_4
joined_str ::= expr . expr expr expr expr BUILD_STRING_5
joined_str ::= expr . expr expr expr expr expr expr BUILD_STRING_7
joined_str ::= expr . expr expr expr expr expr expr expr expr BUILD_STRING_9
joined_str ::= expr expr . BUILD_STRING_2
joined_str ::= expr expr . expr BUILD_STRING_3
joined_str ::= expr expr . expr expr BUILD_STRING_4
joined_str ::= expr expr . expr expr expr BUILD_STRING_5
joined_str ::= expr expr . expr expr expr expr expr BUILD_STRING_7
joined_str ::= expr expr . expr expr expr expr expr expr expr BUILD_STRING_9
joined_str ::= expr expr BUILD_STRING_2 . 
joined_str ::= expr expr expr . BUILD_STRING_3
joined_str ::= expr expr expr . expr BUILD_STRING_4
joined_str ::= expr expr expr . expr expr BUILD_STRING_5
joined_str ::= expr expr expr . expr expr expr expr BUILD_STRING_7
joined_str ::= expr expr expr . expr expr expr expr expr expr BUILD_STRING_9
joined_str ::= expr expr expr BUILD_STRING_3 . 
joined_str ::= expr expr expr expr . BUILD_STRING_4
joined_str ::= expr expr expr expr . expr BUILD_STRING_5
joined_str ::= expr expr expr expr . expr expr expr BUILD_STRING_7
joined_str ::= expr expr expr expr . expr expr expr expr expr BUILD_STRING_9
joined_str ::= expr expr expr expr expr . BUILD_STRING_5
joined_str ::= expr expr expr expr expr . expr expr BUILD_STRING_7
joined_str ::= expr expr expr expr expr . expr expr expr expr BUILD_STRING_9
joined_str ::= expr expr expr expr expr expr . expr BUILD_STRING_7
joined_str ::= expr expr expr expr expr expr . expr expr expr BUILD_STRING_9
joined_str ::= expr expr expr expr expr expr expr . BUILD_STRING_7
joined_str ::= expr expr expr expr expr expr expr . expr expr BUILD_STRING_9
joined_str ::= expr expr expr expr expr expr expr BUILD_STRING_7 . 
joined_str ::= expr expr expr expr expr expr expr expr . expr BUILD_STRING_9
jump_absolute_else ::= come_froms . _jump COME_FROM
jump_absolute_else ::= jb_else . 
jump_forward_else ::= JUMP_FORWARD . 
jump_forward_else ::= JUMP_FORWARD . COME_FROM
jump_forward_else ::= JUMP_FORWARD . ELSE
jump_forward_else ::= JUMP_FORWARD COME_FROM . 
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= _stmts lastl_stmt . 
l_stmts ::= l_stmts . lstmt
l_stmts ::= l_stmts lstmt . 
l_stmts ::= lastl_stmt . 
l_stmts ::= lastl_stmt . come_froms l_stmts
l_stmts ::= lastl_stmt come_froms . l_stmts
l_stmts ::= lastl_stmt come_froms l_stmts . 
l_stmts ::= lstmt . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= ifelsestmtl . 
lastl_stmt ::= iflaststmtl . 
lastl_stmt ::= ifpoplaststmtl . 
lc_setup_finally ::= LOAD_CONST . SETUP_FINALLY
list ::= expr . BUILD_LIST_1
list ::= expr . expr BUILD_LIST_2
list ::= expr . expr expr BUILD_LIST_3
list ::= expr . expr expr expr expr expr expr expr expr BUILD_LIST_9
list ::= expr expr . BUILD_LIST_2
list ::= expr expr . expr BUILD_LIST_3
list ::= expr expr . expr expr expr expr expr expr expr BUILD_LIST_9
list ::= expr expr expr . BUILD_LIST_3
list ::= expr expr expr . expr expr expr expr expr expr BUILD_LIST_9
list ::= expr expr expr expr . expr expr expr expr expr BUILD_LIST_9
list ::= expr expr expr expr expr . expr expr expr expr BUILD_LIST_9
list ::= expr expr expr expr expr expr . expr expr expr BUILD_LIST_9
list ::= expr expr expr expr expr expr expr . expr expr BUILD_LIST_9
list ::= expr expr expr expr expr expr expr expr . expr BUILD_LIST_9
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
named_expr ::= expr . DUP_TOP store
opt_come_from_except ::= _come_froms . 
or ::= and . jitop_come_from_expr COME_FROM
or ::= expr_jt . expr
or ::= expr_jt . expr COME_FROM
or ::= expr_jt expr . 
or ::= expr_jt expr . COME_FROM
or ::= expr_pjit . expr POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr . POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr POP_JUMP_IF_FALSE . COME_FROM
or ::= expr_pjit expr POP_JUMP_IF_FALSE COME_FROM . 
pop_ex_return ::= return_expr . ROT_FOUR POP_EXCEPT RETURN_VALUE
pop_return ::= POP_TOP . return_expr RETURN_VALUE
pop_return ::= POP_TOP return_expr . RETURN_VALUE
popb_return ::= return_expr . POP_BLOCK RETURN_VALUE
pos_arg ::= expr . 
raise_stmt1 ::= expr . RAISE_VARARGS_1
raise_stmt2 ::= expr . expr RAISE_VARARGS_2
raise_stmt2 ::= expr expr . RAISE_VARARGS_2
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_and ::= expr JUMP_IF_FALSE_OR_POP . return_expr_or_cond COME_FROM
ret_and ::= expr JUMP_IF_FALSE_OR_POP return_expr_or_cond . COME_FROM
ret_and ::= expr JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM . 
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return ::= return_expr . discard_tops RETURN_VALUE
return_expr ::= expr . 
return_expr ::= ret_and . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_expr_or_cond ::= return_expr . 
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr . RETURN_END_IF POP_BLOCK
return_if_stmts ::= _stmts . return_if_stmt \e__come_froms
return_if_stmts ::= _stmts . return_if_stmt _come_froms
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
set ::= expr . expr expr BUILD_SET_3
set ::= expr expr . expr BUILD_SET_3
set ::= expr expr expr . BUILD_SET_3
slice2 ::= expr . expr BUILD_SLICE_2
slice2 ::= expr expr . BUILD_SLICE_2
slice2 ::= expr expr BUILD_SLICE_2 . 
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= call_stmt . 
stmt ::= expr_stmt . 
stmt ::= for38 . 
stmt ::= ifelsestmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store ::= unpack . 
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript ::= expr expr BINARY_SUBSCR . 
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
suite_stmts ::= _stmts . 
testexpr ::= testfalse . 
testexpr ::= testtrue . 
testexpr_cf ::= testexpr . come_froms
testexpr_cf ::= testexpr come_froms . 
testexprl ::= testfalsel . 
testfalse ::= and_not . 
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse ::= or . jmp_false COME_FROM
testfalse ::= or jmp_false . COME_FROM
testfalse ::= or jmp_false COME_FROM . 
testfalse ::= testfalse_not_or . 
testfalse_not_and ::= and . jmp_true come_froms
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr jmp_true . COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr . jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr jmp_false . COME_FROM
testfalse_not_or ::= expr jmp_false expr jmp_false COME_FROM . 
testfalsel ::= expr . jmp_true
testfalsel ::= expr jmp_true . 
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
tryfinally38astmt ::= LOAD_CONST . SETUP_FINALLY \e_suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY POP_TOP \e_suite_stmts_opt END_FINALLY POP_TOP
tryfinally38astmt ::= LOAD_CONST . SETUP_FINALLY \e_suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY POP_TOP suite_stmts_opt END_FINALLY POP_TOP
tryfinally38astmt ::= LOAD_CONST . SETUP_FINALLY suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY POP_TOP \e_suite_stmts_opt END_FINALLY POP_TOP
tryfinally38astmt ::= LOAD_CONST . SETUP_FINALLY suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY POP_TOP suite_stmts_opt END_FINALLY POP_TOP
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr . expr expr BUILD_TUPLE_3
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr . expr BUILD_TUPLE_3
tuple ::= expr expr expr . BUILD_TUPLE_3
unary_not ::= expr . UNARY_NOT
unary_not ::= expr UNARY_NOT . 
unary_op ::= expr . unary_operator
unpack ::= UNPACK_SEQUENCE_2 . store store
unpack ::= UNPACK_SEQUENCE_2 store . store
unpack ::= UNPACK_SEQUENCE_2 store store . 
while1stmt ::= \e__come_froms . l_stmts COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= \e__come_froms l_stmts . COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= \e__come_froms l_stmts COME_FROM . JUMP_BACK COME_FROM_LOOP
while1stmt ::= _come_froms . l_stmts COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= _come_froms l_stmts . COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= _come_froms l_stmts COME_FROM . JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= \e__come_froms . l_stmts JUMP_BACK POP_BLOCK
whileTruestmt ::= \e__come_froms l_stmts . JUMP_BACK POP_BLOCK
whileTruestmt ::= _come_froms . l_stmts JUMP_BACK POP_BLOCK
whileTruestmt ::= _come_froms l_stmts . JUMP_BACK POP_BLOCK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= \e__come_froms . pass JUMP_BACK
whileTruestmt38 ::= \e__come_froms \e_pass . JUMP_BACK
whileTruestmt38 ::= \e__come_froms \e_pass JUMP_BACK . 
whileTruestmt38 ::= \e__come_froms l_stmts . JUMP_BACK
whileTruestmt38 ::= \e__come_froms l_stmts . JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= _come_froms . l_stmts JUMP_BACK
whileTruestmt38 ::= _come_froms . l_stmts JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= _come_froms . pass JUMP_BACK
whileTruestmt38 ::= _come_froms \e_pass . JUMP_BACK
whileTruestmt38 ::= _come_froms l_stmts . JUMP_BACK
whileTruestmt38 ::= _come_froms l_stmts . JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts JUMP_BACK
whilestmt38 ::= \e__come_froms . testexpr l_stmts come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr returns POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr . l_stmts JUMP_BACK
whilestmt38 ::= \e__come_froms testexpr . l_stmts come_froms
whilestmt38 ::= \e__come_froms testexpr . l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr . l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr . l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms testexpr . returns POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr \e_l_stmts_opt . COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr \e_l_stmts_opt . JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr \e_l_stmts_opt . JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms testexpr \e_l_stmts_opt COME_FROM . JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr \e_l_stmts_opt JUMP_BACK . POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr \e_l_stmts_opt JUMP_BACK . come_froms
whilestmt38 ::= \e__come_froms testexpr \e_l_stmts_opt JUMP_BACK come_froms . 
whilestmt38 ::= \e__come_froms testexpr l_stmts . JUMP_BACK
whilestmt38 ::= \e__come_froms testexpr l_stmts . come_froms
whilestmt38 ::= \e__come_froms testexpr l_stmts come_froms . 
whilestmt38 ::= \e__come_froms testexpr l_stmts_opt . COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr l_stmts_opt . JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr l_stmts_opt . JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms testexpr l_stmts_opt COME_FROM . JUMP_BACK POP_BLOCK
whilestmt38 ::= _come_froms . testexpr \e_l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= _come_froms . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= _come_froms . testexpr \e_l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= _come_froms . testexpr l_stmts JUMP_BACK
whilestmt38 ::= _come_froms . testexpr l_stmts come_froms
whilestmt38 ::= _come_froms . testexpr l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= _come_froms . testexpr l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= _come_froms . testexpr l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= _come_froms . testexpr returns POP_BLOCK
whilestmt38 ::= _come_froms testexpr . l_stmts JUMP_BACK
whilestmt38 ::= _come_froms testexpr . l_stmts come_froms
whilestmt38 ::= _come_froms testexpr . l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= _come_froms testexpr . l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= _come_froms testexpr . l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= _come_froms testexpr . returns POP_BLOCK
whilestmt38 ::= _come_froms testexpr \e_l_stmts_opt . COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= _come_froms testexpr \e_l_stmts_opt . JUMP_BACK POP_BLOCK
whilestmt38 ::= _come_froms testexpr \e_l_stmts_opt . JUMP_BACK come_froms
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with_as ::= expr . SETUP_WITH store \e_suite_stmts_opt COME_FROM_WITH with_suffix
with_as ::= expr . SETUP_WITH store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH
with_as ::= expr . SETUP_WITH store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with_as ::= expr . SETUP_WITH store suite_stmts POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with_as ::= expr . SETUP_WITH store suite_stmts_opt COME_FROM_WITH with_suffix
with_as ::= expr . SETUP_WITH store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH
with_as ::= expr . SETUP_WITH store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with_as_pass ::= expr . SETUP_WITH store \e_pass POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with_as_pass ::= expr . SETUP_WITH store pass POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
-> 
 L.1501         0  LOAD_FAST                'self'
                   2  LOAD_METHOD              convert_to_docx
                   4  LOAD_FAST                'input_path'
                   6  CALL_METHOD_1         1  '1 positional argument'
                   8  UNPACK_SEQUENCE_2     2 
                  10  STORE_FAST               'processing_path'
                  12  STORE_FAST               'is_from_txt'

import logging, os
from pathlib import Path
import re, shutil, subprocess, sys, tempfile, uuid
from docx import Document
from docx.document import Document as _Document
from docx.enum.table import WD_ROW_HEIGHT_RULE
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.shared import Pt, Cm, RGBColor
from docx.table import Table, _Cell
from docx.text.paragraph import Paragraph
IS_WINDOWS = sys.platform.startswith("win")
IS_LINUX = sys.platform.startswith("linux")
if IS_WINDOWS:
    try:
        import win32com.client
    except ImportError:
        win32com = None

    try:
        import pythoncom
    except ImportError:
        pythoncom = None

else:
    win32com = None
    pythoncom = None
logging.basicConfig(level=(logging.INFO), format="%(asctime)s - %(levelname)s - %(message)s")
BLANK_LINE_MODE_PRESERVE = "不改动任何空行"
BLANK_LINE_MODE_DELETE_SINGLE = "删除单个空行，多个空行保留至1个空行"
BLANK_LINE_MODE_KEEP_SINGLE = "保留单个空行，多个空行保留至1个空行"
BLANK_LINE_MODE_OPTIONS = [
 BLANK_LINE_MODE_PRESERVE,
 BLANK_LINE_MODE_DELETE_SINGLE,
 BLANK_LINE_MODE_KEEP_SINGLE]
DEFAULT_BLANK_LINE_MODE = BLANK_LINE_MODE_DELETE_SINGLE
SUPPORTED_FILE_EXTENSIONS = ('.docx', '.doc', '.wps', '.txt', '.md')
LARGE_FOLDER_FILE_CONFIRM_THRESHOLD = 1000
RE_SAFE_FILENAME_CHARS = re.compile('[<>:"/\\\\|?*\\x00-\\x1f]+')
RE_HAS_CHINESE = re.compile("[\\u4e00-\\u9fff]")
RE_MD_IMAGE = re.compile("!\\[([^\\]]*)\\]\\([^)]+\\)")
RE_MD_LINK = re.compile("\\[([^\\]]+)\\]\\([^)]+\\)")
RE_MD_HTML_TAG = re.compile("<[^>]+>")
RE_MD_INLINE_CODE = re.compile("`([^`]+)`")
RE_MD_BOLD_ASTERISK = re.compile("\\*\\*(.*?)\\*\\*")
RE_MD_BOLD_UNDERSCORE = re.compile("__(.*?)__")
RE_MD_HEADER = re.compile("^\\s*#+\\s+(.*)")
RE_MD_BLOCKQUOTE = re.compile("^\\s*>\\s?(.*)")
RE_MD_HORIZONTAL_RULE = re.compile("^\\s*[-*_]{3,}\\s*$")
RE_MD_UNORDERED_LIST_BLOCK = re.compile("^\\s*[*+-]\\s+")
RE_MD_UNORDERED_LIST = re.compile("^\\s*[*+-]\\s")
RE_MD_BULLET_WITH_CONTENT = re.compile("^(\\s*[*+-]\\s)(.*)")
RE_MD_EMPHASIS_ASTERISK = re.compile("(?<!\\\\)\\*([^\\s*][^*]*?)(?<!\\\\)\\*")
RE_CURRENCY_PREFIX = re.compile("^[¥￥$]")
RE_CURRENCY_SUFFIX = re.compile("(元|万元|亿元)$")
RE_NUMERIC_TABLE_TEXT = re.compile("^[-+]?(?:\\d+(?:\\.\\d+)?|\\.\\d+)%?$")
CHINESE_NUM_PATTERN = "[一二三四五六七八九十百千万零]+"
RE_TITLE_H1 = re.compile("^" + CHINESE_NUM_PATTERN + "\\s*、")
RE_TITLE_H2 = re.compile("^[（\\(]" + CHINESE_NUM_PATTERN + "[）\\)]")
RE_HEADING_H1 = re.compile("^[一二三四五六七八九十百千万零]+\\s*、")
RE_HEADING_H2 = re.compile("^[（\\(][一二三四五六七八九十百千万零]+[）\\)]")
RE_HEADING_H3 = re.compile("^\\d+\\s*[\\.．]")
RE_HEADING_H4 = re.compile("^[（\\(]\\d+[）\\)]")
RE_ATTACHMENT = re.compile("^附件\\s*(\\d+|[一二三四五六七八九十百千万零]+)?\\s*[:：]?$")
RE_H2_INLINE_TITLE = re.compile("^[（\\(](.+?)[）\\)](.*)", re.DOTALL)

class LegacyConversionUnavailable(RuntimeError):
    __doc__ = "Raised when an old Word/WPS file is intentionally skipped."


class SofficeConverter:
    __doc__ = "LibreOffice wrapper for converting legacy .doc/.wps files to .docx."

    def __init__(self, soffice_path=None, timeout=120):
        self.soffice_path = soffice_path or self._find_soffice()
        self.timeout = int(timeout or 120)

    @property
    def available(self):
        return bool(self.soffice_path)

    @staticmethod
    def _find_soffice():
        for executable in ('soffice', 'soffice.com', 'libreoffice'):
            found = shutil.which(executable)
            if found:
                return found
            common_paths = []
            if sys.platform == "darwin":
                common_paths.extend([
                 "/Applications/LibreOffice.app/Contents/MacOS/soffice",
                 "/opt/homebrew/bin/soffice",
                 "/usr/local/bin/soffice"])
            else:
                if os.name == "nt":
                    for base in (
                     os.environ.get("PROGRAMFILES"), os.environ.get("PROGRAMFILES(X86)")):
                        if base:
                            common_paths.extend([
                             os.path.join(base, "LibreOffice", "program", "soffice.com"),
                             os.path.join(base, "LibreOffice", "program", "soffice.exe")])

                else:
                    common_paths.extend([
                     '/usr/bin/soffice', 
                     '/usr/local/bin/soffice', 
                     '/usr/bin/libreoffice', 
                     '/usr/local/bin/libreoffice', 
                     '/snap/bin/libreoffice', 
                     '/opt/libreoffice/program/soffice', 
                     '/opt/libreoffice*/program/soffice'])
            for path in common_paths:
                if "*" in path:
                    for candidate in sorted(Path("/").glob(path.lstrip("/"))):
                        if candidate.is_file():
                            return str(candidate)

                else:
                    if path and os.path.isfile(path):
                        return path
                    return

    def convert_to_docx(self, input_path, log=None):
        input_path = Path(input_path).expanduser().resolve()
        if not self.available:
            raise RuntimeError(f"LibreOffice (soffice) 不可用，无法转换 {input_path}。请安装 LibreOffice，或先将文档另存为 .docx 后再处理。")
        work_dir = Path(tempfile.mkdtemp(prefix="wfp_soffice_"))
        out_dir = work_dir / "out"
        profile_dir = work_dir / "profile"
        out_dir.mkdir(parents=True, exist_ok=True)
        profile_dir.mkdir(parents=True, exist_ok=True)
        profile_uri = profile_dir.resolve().as_posix()
        if os.name == "nt":
            profile_uri = "/" + profile_uri
        cmd = [
         self.soffice_path,
         "--headless",
         "--norestore",
         f"-env:UserInstallation=file://{profile_uri}",
         "--convert-to",
         "docx",
         "--outdir",
         str(out_dir),
         str(input_path)]
        if log:
            log(f"  > 正在使用 LibreOffice 转换为 .docx: {input_path.name}")
        creationflags = 0
        if os.name == "nt":
            if hasattr(subprocess, "CREATE_NO_WINDOW"):
                creationflags = subprocess.CREATE_NO_WINDOW
        try:
            proc = subprocess.run(cmd,
              stdout=(subprocess.PIPE),
              stderr=(subprocess.PIPE),
              text=True,
              timeout=(self.timeout),
              creationflags=creationflags,
              check=False)
        except subprocess.TimeoutExpired as exc:
            try:
                shutil.rmtree(work_dir, ignore_errors=True)
                raise RuntimeError(f"LibreOffice 转换超时 ({self.timeout}s): {input_path}") from exc
            finally:
                exc = None
                del exc

        except FileNotFoundError as exc:
            try:
                shutil.rmtree(work_dir, ignore_errors=True)
                raise RuntimeError(f"找不到 soffice 可执行文件: {self.soffice_path}") from exc
            finally:
                exc = None
                del exc

        except Exception:
            shutil.rmtree(work_dir, ignore_errors=True)
            raise
        else:
            if proc.returncode != 0:
                detail = (proc.stderr or proc.stdout or "").strip()
                shutil.rmtree(work_dir, ignore_errors=True)
                raise RuntimeError(f"LibreOffice 无法将 {input_path} 转为 .docx。请先手动转为 .docx 后再处理。详细错误: {detail}")
            generated_files = sorted(out_dir.glob("*.docx"))
            if not generated_files:
                detail = (proc.stderr or proc.stdout or "").strip()
                shutil.rmtree(work_dir, ignore_errors=True)
                raise RuntimeError(f"LibreOffice 未生成 {input_path} 对应的 .docx。请先手动转为 .docx 后再处理。详细信息: {detail}")
            if log:
                log(f"  > LibreOffice 转换完成: {generated_files[0].name}")
            return (
             generated_files[0], work_dir)


def _initialize_com_for_threadParse error at or near `LOAD_GLOBAL' instruction at offset 0


def _uninitialize_com_for_thread(initialized, log_callback=None):
    if not initialized or pythoncom is None:
        return
    try:
        pythoncom.CoUninitialize()
    except Exception as e:
        try:
            if log_callback:
                log_callback(f"警告：后台线程释放 COM 失败：{e}")
        finally:
            e = None
            del e


class WPSAppManager:

    def __init__(self, log_callback=None):
        self.log_callback = log_callback
        self.com_app = None

    def _log(self, message):
        if self.log_callback:
            self.log_callback(message)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit()
        return False

    @staticmethod
    def _com_available():
        return IS_WINDOWS and win32com is not None

    @staticmethod
    def _com_unavailable_message(file_ext=None):
        if file_ext in ('.doc', '.wps'):
            return f"当前环境无法使用 WPS/Word COM 直接转换 {file_ext} 文件。程序会改用 LibreOffice soffice 转换；如 soffice 不可用，请安装 LibreOffice，或先将文件另存为 .docx 后再处理。"
        return "当前环境无法使用 WPS/Word COM 自动化，已跳过接受修订和自动编号转文本。在 Linux/Kylin 等系统上这是预期行为。"

    def get_app(self):
        if not self._com_available():
            raise RuntimeError(self._com_unavailable_message())
        if self.com_app is None:
            self._log("首次需要，正在启动WPS/Word应用（独立进程）...")
            try:
                self.com_app = win32com.client.DispatchEx("KWPS.Application")
                self._log("  > 已成功连接到WPS。")
            except Exception:
                try:
                    self.com_app = win32com.client.DispatchEx("Word.Application")
                    self._log("  > 已成功连接到Word。")
                except Exception as e:
                    try:
                        raise RuntimeError(f"未能启动WPS或Word，请确保已安装。错误: {e}")
                    finally:
                        e = None
                        del e

            try:
                self.com_app.Visible = False
            except Exception:
                pass
            else:
                try:
                    self.com_app.DisplayAlerts = False
                except Exception:
                    pass

        return self.com_app

    def quit(self):
        if self.com_app:
            self._log("所有任务完成，正在关闭WPS/Word应用...")
            try:
                try:
                    self.com_app.Quit()
                except Exception as e:
                    try:
                        self._log(f"  > 警告：关闭应用时发生异常: {e}")
                    finally:
                        e = None
                        del e

            finally:
                self.com_app = None
                self._log("  > 应用已关闭。")


class WordProcessor:

    def __init__(self, config, log_callback=None, remove_blank_lines=True, blank_line_mode=None, com_manager=None, soffice_path=None, soffice_timeout=120):
        self.config = config
        self.temp_files = []
        self.sys_temp_dir = tempfile.gettempdir()
        self.log_callback = log_callback
        self.com_manager = com_manager or WPSAppManager(log_callback)
        self._owns_com_manager = com_manager is None
        self.soffice_path = soffice_path
        self.soffice_timeout = soffice_timeout
        self.soffice_converter = None
        self.blank_line_mode = self._normalize_blank_line_mode((blank_line_mode or self.config.get("blank_line_mode")),
          remove_blank_lines=remove_blank_lines)
        self.remove_blank_lines = self.blank_line_mode == BLANK_LINE_MODE_DELETE_SINGLE

    def _log(self, message):
        if self.log_callback:
            self.log_callback(message)

    @staticmethod
    def _com_available():
        return WPSAppManager._com_available()

    @staticmethod
    def _com_unavailable_message(file_ext=None):
        return WPSAppManager._com_unavailable_message(file_ext)

    @staticmethod
    def _paragraph_has_ooxml(para, tag_name):
        return para._p.find(".//" + qn(tag_name)) is not None

    @classmethod
    def _has_field_codes(cls, para):
        return cls._paragraph_has_ooxml(para, "w:fldChar") or cls._paragraph_has_ooxml(para, "w:instrText")

    @classmethod
    def _has_drawing_or_pict(cls, para):
        return cls._paragraph_has_ooxml(para, "w:drawing") or cls._paragraph_has_ooxml(para, "w:pict")

    @classmethod
    def _has_embedded_object(cls, para):
        return cls._paragraph_has_ooxml(para, "w:object")

    @staticmethod
    def _normalize_blank_line_mode(mode, remove_blank_lines=True):
        if mode in BLANK_LINE_MODE_OPTIONS:
            return mode
        if mode in ('preserve', 'none'):
            return BLANK_LINE_MODE_PRESERVE
        if mode in ('delete_single', 'remove_single'):
            return BLANK_LINE_MODE_DELETE_SINGLE
        if mode in ('keep_single', 'compress'):
            return BLANK_LINE_MODE_KEEP_SINGLE
        if isinstance(mode, bool):
            if mode:
                return BLANK_LINE_MODE_DELETE_SINGLE
            return BLANK_LINE_MODE_KEEP_SINGLE
        if remove_blank_lines:
            return BLANK_LINE_MODE_DELETE_SINGLE
        return BLANK_LINE_MODE_KEEP_SINGLE

    def _cleanup_temp_files(self):
        if not self.temp_files:
            return
        self._log("正在清理本轮临时文件...")
        for f in self.temp_files:
            try:
                if os.path.exists(f):
                    os.remove(f)
                    self._log(f"  > 临时文件 {os.path.basename(f)} 已删除")
            except OSError as e:
                try:
                    self._log(f"  > 警告：删除临时文件 {f} 失败: {e}")
                finally:
                    e = None
                    del e

        else:
            self.temp_files.clear()

    def _make_temp_docx_path(self, prefix, base_name):
        safe_base_name = RE_SAFE_FILENAME_CHARS.sub("_", base_name).strip(" ._")
        safe_base_name = (safe_base_name or "document")[None[:80]]
        temp_name = f"~temp_{prefix}_{safe_base_name}_{os.getpid()}_{uuid.uuid4().hex[None[:8]]}.docx"
        temp_path = os.path.join(self.sys_temp_dir, temp_name)
        self.temp_files.append(temp_path)
        return temp_path

    def _get_wps_app(self):
        return self.com_manager.get_app()

    def _get_soffice_converter(self):
        if self.soffice_converter is None:
            self.soffice_converter = SofficeConverter(self.soffice_path, self.soffice_timeout)
        return self.soffice_converter

    def _convert_legacy_with_com(self, input_path, temp_docx_path):
        app = self._get_wps_app()
        doc_com = None
        try:
            doc_com = app.Documents.Open((os.path.abspath(input_path)), ReadOnly=1)
            doc_com.SaveAs2((os.path.abspath(temp_docx_path)), FileFormat=12)
        finally:
            if doc_com is not None:
                doc_com.Close()

        self._log("文件格式转换完成。")

    def _convert_legacy_with_soffice(self, input_path, temp_docx_path):
        converter = self._get_soffice_converter()
        if not converter.available:
            raise LegacyConversionUnavailable(f"{self._com_unavailable_message(os.path.splitext(input_path)[1].lower())} 已跳过该旧格式文件，继续处理其他可支持文件。")
        converted_path, work_dir = converter.convert_to_docx(input_path, self._log)
        try:
            shutil.copy2(converted_path, temp_docx_path)
        finally:
            shutil.rmtree(work_dir, ignore_errors=True)

        self._log("LibreOffice 文件格式转换完成。")

    def quit_com_app(self):
        if self._owns_com_manager:
            self.com_manager.quit()

    @staticmethod
    def _has_chinese(text):
        return bool(RE_HAS_CHINESE.search(text or ""))

    @staticmethod
    def _is_digit_or_latin(ch):
        if not ch:
            return False
        code = ord(ch)
        return ch.isdigit() or "A" <= ch <= "Z" or "a" <= ch <= "z" or 65296 <= code <= 65305 or 65313 <= code <= 65338 or 65345 <= code <= 65370

    @staticmethod
    def _prev_non_space(text, index):
        i = index - 1
        while i >= 0:
            if text[i].isspace():
                i -= 1

        if i >= 0:
            return text[i]
        return ""

    @staticmethod
    def _next_non_space(text, index):
        i = index + 1
        while i < len(text):
            if text[i].isspace():
                i += 1

        if i < len(text):
            return text[i]
        return ""

    @classmethod
    def _is_after_digit_or_latin(cls, text, index):
        return cls._is_digit_or_latin(cls._prev_non_space(text, index))

    @classmethod
    def _is_before_digit_or_latin(cls, text, index):
        return cls._is_digit_or_latin(cls._next_non_space(text, index))

    @classmethod
    def _normalize_ellipsis(cls, text):
        dot_chars = {".", "．", "。"}
        chars = []
        i = 0
        while i < len(text):
            ch = text[i]
            if ch not in dot_chars:
                chars.append(ch)
                i += 1
            else:
                j = i + 1
                if j < len(text) and text[j] in dot_chars:
                    j += 1
                else:
                    if j - i >= 3:
                        cls._is_after_digit_or_latin(text, i) or chars.append("……")
                    else:
                        chars.append(text[i[:j]])
                    i = j

        return "".join(chars)

    @classmethod
    def _normalize_simple_punctuationParse error at or near `COLLECTION_START' instruction at offset 0_0

    @classmethod
    def _normalize_bracket_pairs(cls, text):
        pair_sets = [
         (
          {'(':"（", 
           '（':"（"}, {')':"）",  '）':"）"}),
         (
          {'[':"［", 
           '［':"［"}, {']':"］",  '］':"］"})]
        result = text
        for open_chars, close_chars in pair_sets:
            chars = list(result)
            stack = []

        for i, ch in enumerate(chars):
            if ch in open_chars:
                stack.append(i)
            else:
                if ch in close_chars:
                    if stack:
                        open_index = stack.pop()
                        content = "".join(chars[(open_index + 1)[:i]])
                        if not cls._has_chinese(content):
                            pass
                        elif cls._is_after_digit_or_latin(result, open_index):
                            pass
                        elif cls._is_before_digit_or_latin(result, i):
                            pass
                        else:
                            chars[open_index] = open_chars[chars[open_index]]
                            chars[i] = close_chars[ch]
                    result = "".join(chars)
                return result

    @classmethod
    def _normalize_quote_pairs(cls, text, quote_chars, left_quote, right_quote, skip_inner_latin=False):
        chars = list(text)
        open_index = None
        for i, ch in enumerate(chars):
            if ch not in quote_chars:
                pass
            else:
                prev_is_latin = cls._is_after_digit_or_latin(text, i)
                next_is_latin = cls._is_before_digit_or_latin(text, i)
                if skip_inner_latin and prev_is_latin and next_is_latin:
                    pass
                elif open_index is None:
                    if prev_is_latin:
                        pass
                    else:
                        open_index = i
                else:
                    content = "".join(chars[(open_index + 1)[:i]])
                    should_normalize = cls._has_chinese(content) and not cls._is_after_digit_or_latin(text, open_index) and not cls._is_before_digit_or_latin(text, i)
                    if should_normalize:
                        chars[open_index] = left_quote
                        chars[i] = right_quote
                    open_index = None
        else:
            return "".join(chars)

    @classmethod
    def _normalize_symbols_in_text(cls, text):
        return text and cls._has_chinese(text) or text
        result = cls._normalize_bracket_pairs(text)
        result = cls._normalize_ellipsis(result)
        result = cls._normalize_quote_pairs(result, {
         '"', '“', '”', '„', '‟', '「', '」'}, "“", "”")
        result = cls._normalize_quote_pairs(result,
          {
         "'", '‘', '’', '‚', '‛'},
          "‘",
          "’",
          skip_inner_latin=True)
        result = cls._normalize_simple_punctuation(result)
        return result

    @staticmethod
    def _redistribute_text_to_runs(runs, new_full_text):
        if not runs:
            return
        run_lengths = [len(run.text) for run in runs]
        if len(new_full_text) == sum(run_lengths):
            pos = 0
            for run, length in zip(runs, run_lengths):
                run.text = new_full_text[pos[:pos + length]]
                pos += length
            else:
                return

        runs[0].text = new_full_text
        for run in runs[1[:None]]:
            run.text = ""

    def _normalize_paragraph_symbols(self, para):
        text = para.text
        return text.strip() and para.runs or False
        if self._has_field_codes(para):
            return False
        normalized = self._normalize_symbols_in_text(text)
        if normalized == text:
            return False
        self._redistribute_text_to_runs(para.runs, normalized)
        return True

    def _normalize_document_symbols(self, doc):
        changes = 0
        for para in doc.paragraphs:
            if self._normalize_paragraph_symbols(para):
                changes += 1
            for table in doc.tables:
                for row in table.rows:
                    for cell in row.cells:
                        for para in cell.paragraphs:
                            if self._normalize_paragraph_symbols(para):
                                changes += 1

                    else:
                        return changes

    @staticmethod
    def _clean_markdown(text):
        """
        Clean Markdown content to plain text:
        1. Remove images, links, HTML, inline code markers
        2. Remove bold/italic markers (*, **, __)
        3. Remove heading markers (#)
        4. Remove blockquote markers (>)
        5. Remove horizontal rules (---)
        6. Preserve original ordered-list numbering from the source text
        """
        if not text:
            return ""
        text = RE_MD_IMAGE.sub("\\1", text)
        text = RE_MD_LINK.sub("\\1", text)
        text = RE_MD_HTML_TAG.sub("", text)
        text = RE_MD_INLINE_CODE.sub("\\1", text)
        text = RE_MD_BOLD_ASTERISK.sub("\\1", text)
        text = RE_MD_BOLD_UNDERSCORE.sub("\\1", text)
        lines = text.split("\n")
        new_lines = []
        for line in lines:
            cleaned_line = line
            header_match = RE_MD_HEADER.match(cleaned_line)
            if header_match:
                cleaned_line = header_match.group(1)
            else:
                blockquote_match = RE_MD_BLOCKQUOTE.match(cleaned_line)
                if blockquote_match:
                    cleaned_line = blockquote_match.group(1)
                if RE_MD_HORIZONTAL_RULE.match(cleaned_line):
                    cleaned_line = ""
                is_bullet = RE_MD_UNORDERED_LIST.match(cleaned_line)

                def remove_stars(m):
                    return m.group(1)

                if is_bullet:
                    bullet_match = RE_MD_BULLET_WITH_CONTENT.match(cleaned_line)
                    if bullet_match:
                        marker = bullet_match.group(1)
                        content = bullet_match.group(2)
                        content = RE_MD_EMPHASIS_ASTERISK.sub(remove_stars, content)
                        cleaned_line = marker + content
                else:
                    cleaned_line = RE_MD_EMPHASIS_ASTERISK.sub(remove_stars, cleaned_line)
            new_lines.append(cleaned_line)
        else:
            return "\n".join(new_lines)

    @staticmethod
    def _remove_blank_lines_from_text(text, keep_single_blank_lines=False):
        """
        Normalize blank lines from txt/md text:
        - 2+ consecutive blank lines: merge to 1
        - Single blank line: delete by default, or keep when requested
        """
        if not text:
            return text
        lines = text.split("\n")
        result = []
        blank_count = 0
        for line in lines:
            if line.strip() == "":
                blank_count += 1
            elif not blank_count >= 2:
                if blank_count == 1:
                    if keep_single_blank_lines:
                        result.append("")
                result.append(line)
                blank_count = 0
            if (blank_count >= 2 or blank_count) == 1:
                if keep_single_blank_lines:
                    result.append("")
            return "\n".join(result)

    def _normalize_text_blank_lines(self, text):
        if self.blank_line_mode == BLANK_LINE_MODE_PRESERVE:
            return text
        return self._remove_blank_lines_from_text(text,
          keep_single_blank_lines=(self.blank_line_mode == BLANK_LINE_MODE_KEEP_SINGLE))

    def _log_blank_line_mode(self, source_name):
        if self.blank_line_mode == BLANK_LINE_MODE_PRESERVE:
            self._log(f"  > 未改动 {source_name} 中的空行。")
        else:
            if self.blank_line_mode == BLANK_LINE_MODE_KEEP_SINGLE:
                self._log(f"  > 已保留 {source_name} 中的单个空行，并将多个空行合并为 1 个。")
            else:
                self._log(f"  > 已删除 {source_name} 中的单个空行，并将多个空行合并为 1 个。")

    @staticmethod
    def _read_text_fileParse error at or near `LOAD_CONST' instruction at offset 0

    def convert_to_docx(self, input_path):
        file_ext = os.path.splitext(input_path)[1].lower()
        is_from_txt = file_ext in ('.txt', '.md')
        base_name = os.path.splitext(os.path.basename(input_path))[0]
        if file_ext == ".docx":
            self._log("检测到 .docx 文件，正在创建安全的处理副本...")
            temp_docx_path = self._make_temp_docx_path("copy", base_name)
            shutil.copy2(input_path, temp_docx_path)
            self._log(f"  > 副本创建成功: {os.path.basename(temp_docx_path)}")
            return (temp_docx_path, False)
        temp_docx_path = self._make_temp_docx_path("converted", base_name)
        if file_ext == ".txt":
            self._log("检测到 .txt 文件，正在创建 .docx...")
            text_content = self._read_text_file(input_path)
            text_content = self._normalize_text_blank_lines(text_content)
            self._log_blank_line_mode("TXT")
            doc = Document()
            for line in text_content.split("\n"):
                doc.add_paragraph(line.strip())
            else:
                doc.save(temp_docx_path)
                self._log("TXT转换完成。")
                return (temp_docx_path, is_from_txt)

        if file_ext == ".md":
            self._log("检测到 .md 文件，正在清理 Markdown 标记并创建 .docx...")
            raw_text = self._read_text_file(input_path)
            cleaned_text = self._clean_markdown(raw_text)
            cleaned_text = self._normalize_text_blank_lines(cleaned_text)
            self._log_blank_line_mode("Markdown 文本")
            doc = Document()
            for line in cleaned_text.split("\n"):
                doc.add_paragraph(line.strip())
            else:
                doc.save(temp_docx_path)
                self._log("Markdown 转换完成。")
                return (temp_docx_path, is_from_txt)

        if file_ext in ('.wps', '.doc'):
            self._log(f"正在转换 {file_ext} 文件为 .docx...")
            if self._com_available():
                try:
                    self._convert_legacy_with_com(input_path, temp_docx_path)
                    return                     return (
                     temp_docx_path, is_from_txt)
                            except Exception as exc:
                    try:
                        self._log(f"  > WPS/Word 转换失败，尝试使用 LibreOffice 兜底: {exc}")
                    finally:
                        exc = None
                        del exc

            else:
                self._log(f"  > {self._com_unavailable_message(file_ext)}")
            self._convert_legacy_with_soffice(input_path, temp_docx_path)
            return (temp_docx_path, is_from_txt)
        raise ValueError(f"不支持的文件格式: {file_ext}")

    def _preprocess_com_tasks(self, docx_path):
        if not self._com_available():
            self._log(f"  > {self._com_unavailable_message()}")
            return
        self._log("正在对副本执行预处理（接受所有修订、转换自动编号）...")
        doc_com = None
        try:
            try:
                app = self._get_wps_app()
                doc_com = app.Documents.Open(os.path.abspath(docx_path))
                doc_com.TrackRevisions = False
                self._log("  > 已关闭修订追踪。")
                if doc_com.Revisions.Count > 0:
                    doc_com.AcceptAllRevisions()
                    self._log("  > 已接受文档副本中的所有修订。")
                doc_com.Content.ListFormat.ConvertNumbersToText()
                self._log("  > 已将副本中的自动编号转换为文本。")
                if doc_com.Revisions.Count > 0:
                    doc_com.AcceptAllRevisions()
                    self._log("  > 已接受编号转换产生的修订。")
                doc_com.TrackRevisions = False
                doc_com.Save()
                self._log("预处理完成。")
            except Exception as e:
                try:
                    self._log(f"警告：执行预处理任务时出错: {e}")
                finally:
                    e = None
                    del e

        finally:
            if doc_com is not None:
                try:
                    doc_com.Close()
                except Exception as e:
                    try:
                        self._log(f"  > 警告：关闭预处理文档时发生异常: {e}")
                    finally:
                        e = None
                        del e

    def _create_page_number(self, paragraph, text):
        font_name = self.config["page_number_font"]
        font_size = self.config["page_number_size"]
        self._set_run_font((paragraph.add_run("— ")), font_name, font_size, set_color=True)
        run_field = paragraph.add_run()
        self._set_run_font(run_field, font_name, font_size, set_color=True)
        fldChar1 = OxmlElement("w:fldChar")
        fldChar1.set(qn("w:fldCharType"), "begin")
        instrText = OxmlElement("w:instrText")
        instrText.set(qn("xml:space"), "preserve")
        instrText.text = text
        fldChar2 = OxmlElement("w:fldChar")
        fldChar2.set(qn("w:fldCharType"), "end")
        run_field._r.extend([fldChar1, instrText, fldChar2])
        self._set_run_font((paragraph.add_run(" —")), font_name, font_size, set_color=True)

    def _apply_page_setup(self, doc, is_from_txt=False):
        self._log("正在应用页面边距和页码设置...")
        should_set_a4 = is_from_txt or self.config.get("force_a4", False)
        for section in doc.sections:
            section.top_margin = Cm(self.config["margin_top"])
            section.bottom_margin = Cm(self.config["margin_bottom"])
            section.left_margin = Cm(self.config["margin_left"])
            section.right_margin = Cm(self.config["margin_right"])
            section.footer_distance = Cm(self.config["footer_distance"])
            if should_set_a4:
                section.page_width = Cm(21)
                section.page_height = Cm(29.7)
            if self.config["page_number_align"] == "居中":
                p = section.footer.paragraphs[0] if section.footer.paragraphs else section.footer.add_paragraph()
                p.clear()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                self._create_page_number(p, "PAGE")
        else:
            if self.config["page_number_align"] == "奇偶分页":
                doc.settings.odd_and_even_pages_header_footer = True
                footer_odd = section.footer
                p_odd = footer_odd.paragraphs[0] if footer_odd.paragraphs else footer_odd.add_paragraph()
                p_odd.clear()
                p_odd.alignment = WD_ALIGN_PARAGRAPH.RIGHT
                self._create_page_number(p_odd, "PAGE")
                footer_even = section.even_page_footer
                p_even = footer_even.paragraphs[0] if footer_even.paragraphs else footer_even.add_paragraph()
                p_even.clear()
                p_even.alignment = WD_ALIGN_PARAGRAPH.LEFT
                self._create_page_number(p_even, "PAGE")
            if should_set_a4:
                self._log("  > 已将页面大小设置为 A4。")

    def _set_run_font(self, run, font_name, size_pt, set_color=False):
        run.font.size = Pt(size_pt)
        if set_color:
            run.font.color.rgb = RGBColor(0, 0, 0)
        rPr = run._r.get_or_add_rPr()
        rFonts = rPr.get_or_add_rFonts()
        for theme_attr in ('w:eastAsiaTheme', 'w:asciiTheme', 'w:hAnsiTheme', 'w:cstheme',
                           'w:csTheme'):
            rFonts.attrib.pop(qn(theme_attr), None)
        else:
            rFonts.set(qn("w:eastAsia"), font_name)
            en_font = self.config.get("english_font") if self.config.get("use_custom_english_font", False) else font_name
            en_font = en_font or font_name
            run.font.name = en_font
            rFonts.set(qn("w:ascii"), en_font)
            rFonts.set(qn("w:hAnsi"), en_font)

    def _apply_font_to_runs(self, para, font_name, size_pt, set_color=False):
        for run in para.runs:
            self._set_run_font(run, font_name, size_pt, set_color=set_color)

    def _get_paragraph_font_info(self, para):
        """获取段落主要字体和字号信息"""
        if not para.runs:
            return (None, None)
        for run in para.runs:
            if run.text.strip():
                font_name = run.font.name
                font_size = run.font.size.pt if run.font.size else None
                return (font_name, font_size)
            return (None, None)

    def _strip_leading_whitespace(self, para):
        if not para.runs:
            return
        else:
            while para.runs:
                first_run = para.runs[0]
                r_elem = first_run._r
                children = [child for child in r_elem if child.tag != qn("w:rPr")]
                only_text = all((child.tag == qn("w:t") for child in ))
                if only_text:
                    if first_run.text.strip():
                        break
                    para._p.remove(r_elem)

            return para.runs or None
        first_run = para.runs[0]
        original_text = first_run.text
        stripped_text = original_text.lstrip()
        if original_text != stripped_text:
            first_run.text = stripped_text
            self._log("  > 已移除段落前的多余空格。")

    def _reset_pagination_properties(self, para):
        para.paragraph_format.widow_control = False
        para.paragraph_format.keep_with_next = False
        para.paragraph_format.keep_lines_together = False
        para.paragraph_format.page_break_before = False
        para.paragraph_format.keep_together = False

    def _get_outline_level(self, para):
        """
        读取段落的当前大纲级别
        返回: 0-8 表示级别1-9，None 表示未设置
        """
        pPr = para._p.get_or_add_pPr()
        outlineLvl = pPr.find(qn("w:outlineLvl"))
        if outlineLvl is not None:
            val = outlineLvl.get(qn("w:val"))
            if val is not None:
                return int(val)
        return

    def _set_outline_level(self, para, level):
        """
        直接设置段落的大纲级别，不通过样式，不影响字体字号等格式
        level: 1-9 的整数，表示大纲级别
        返回: 原有的大纲级别 (0-8) 或 None
        """
        if level < 1 or level > 9:
            self._log(f"  > 警告：大纲级别 {level} 超出范围 (1-9)，已跳过设置")
            return
        original_level = self._get_outline_level(para)
        pPr = para._p.get_or_add_pPr()
        outlineLvl = pPr.find(qn("w:outlineLvl"))
        if outlineLvl is None:
            outlineLvl = OxmlElement("w:outlineLvl")
            pPr.append(outlineLvl)
        outlineLvl.set(qn("w:val"), str(level - 1))
        return original_level

    def _format_heading(self, para, level):
        """
        为段落设置大纲级别（仅设置大纲级别，不影响其他格式）
        """
        if not self.config["set_outline"]:
            self._log("  > 大纲级别设置已禁用，跳过")
            return
        else:
            text_preview = para.text.strip()[None[:30]].replace("\n", " ")
            original_level = self._set_outline_level(para, level)
            if original_level is not None:
                self._log(f'  > 大纲级别: Lv{original_level + 1} → Lv{level} (覆盖) - "{text_preview}..."')
            else:
                self._log(f'  > 大纲级别: 无 → Lv{level} (新设) - "{text_preview}..."')

    def _apply_text_indent_and_align(self, para):
        pf = para.paragraph_format
        pf.first_line_indent = None
        pf.left_indent = Cm(self.config["left_indent_cm"])
        pf.right_indent = Cm(self.config["right_indent_cm"])
        ind = para._p.get_or_add_pPr().get_or_add_ind()
        ind.attrib.pop(qn("w:leftChars"), None)
        ind.attrib.pop(qn("w:hanging"), None)
        ind.attrib.pop(qn("w:hangingChars"), None)
        ind.attrib.pop(qn("w:firstLine"), None)
        ind.set(qn("w:firstLineChars"), "200")
        para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    def _iter_block_items(self, parent):
        parent_elm = parent.element.body if isinstance(parent, _Document) else parent._tc
        for child in parent_elm.iterchildren():
            if isinstance(child, CT_P):
                yield Paragraph(child, parent)
            elif isinstance(child, CT_Tbl):
                yield Table(child, parent)

    def _get_or_add_table_pr(self, table):
        tbl = table._tbl
        tbl_pr = tbl.tblPr
        if tbl_pr is None:
            tbl_pr = OxmlElement("w:tblPr")
            tbl.insert(0, tbl_pr)
        return tbl_pr

    def _set_table_borders(self, table, size_pt=0.5, color='000000'):
        size = max(1, int(float(size_pt) * 8))
        tbl_pr = self._get_or_add_table_pr(table)
        borders = tbl_pr.find(qn("w:tblBorders"))
        if borders is None:
            borders = OxmlElement("w:tblBorders")
            tbl_pr.append(borders)
        else:
            for child in list(borders):
                borders.remove(child)
            else:
                for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
                    elem = OxmlElement(f"w:{edge}")
                    elem.set(qn("w:val"), "single")
                    elem.set(qn("w:sz"), str(size))
                    elem.set(qn("w:space"), "0")
                    elem.set(qn("w:color"), color)
                    borders.append(elem)

    def _set_cell_borders(self, cell, size_pt=0.5, color='000000'):
        size = max(1, int(float(size_pt) * 8))
        tc = cell._tc
        tc_pr = tc.tcPr
        if tc_pr is None:
            tc_pr = OxmlElement("w:tcPr")
            tc.insert(0, tc_pr)
        borders = tc_pr.find(qn("w:tcBorders"))
        if borders is None:
            borders = OxmlElement("w:tcBorders")
            tc_pr.append(borders)
        else:
            for child in list(borders):
                borders.remove(child)
            else:
                for edge in ('top', 'left', 'bottom', 'right'):
                    elem = OxmlElement(f"w:{edge}")
                    elem.set(qn("w:val"), "single")
                    elem.set(qn("w:sz"), str(size))
                    elem.set(qn("w:space"), "0")
                    elem.set(qn("w:color"), color)
                    borders.append(elem)

    def _set_table_cell_margins(self, table, top_cm=0.0, bottom_cm=0.0, left_cm=0.05, right_cm=0.05):
        tbl_pr = self._get_or_add_table_pr(table)
        cell_mar = tbl_pr.find(qn("w:tblCellMar"))
        if cell_mar is None:
            cell_mar = OxmlElement("w:tblCellMar")
            tbl_pr.append(cell_mar)

        def set_side(tag, cm_value):
            node = cell_mar.find(qn(f"w:{tag}"))
            if node is None:
                node = OxmlElement(f"w:{tag}")
                cell_mar.append(node)
            node.set(qn("w:type"), "dxa")
            node.set(qn("w:w"), str(int(Cm(float(cm_value)).twips)))

        set_side("top", top_cm)
        set_side("bottom", bottom_cm)
        set_side("left", left_cm)
        set_side("right", right_cm)

    def _set_table_width_percent(self, table, percent=100):
        percent = max(1, min(100, int(float(percent))))
        tbl_pr = self._get_or_add_table_pr(table)
        tbl_w = tbl_pr.find(qn("w:tblW"))
        if tbl_w is None:
            tbl_w = OxmlElement("w:tblW")
            tbl_pr.append(tbl_w)
        tbl_w.set(qn("w:type"), "pct")
        tbl_w.set(qn("w:w"), str(percent * 50))

    def _set_table_indent(self, table, indent_twips=0):
        tbl_pr = self._get_or_add_table_pr(table)
        tbl_ind = tbl_pr.find(qn("w:tblInd"))
        if tbl_ind is None:
            tbl_ind = OxmlElement("w:tblInd")
            tbl_pr.append(tbl_ind)
        tbl_ind.set(qn("w:type"), "dxa")
        tbl_ind.set(qn("w:w"), str(int(indent_twips)))

    @staticmethod
    def _table_text_weight(text):
        weight = 0.0
        for ch in text:
            weight += 0.5 if ord(ch) < 128 else 1.0
        else:
            return weight

    @staticmethod
    def _normalize_table_pcts(weights, min_pct, max_pct):
        total = sum(weights) or 1.0
        pcts = [w / total * 100 for w in weights]
        for i, value in enumerate(pcts):
            if value < min_pct:
                pcts[i] = min_pct
            else:
                if value > max_pct:
                    pcts[i] = max_pct
                total = sum(pcts) or 1.0
                return [value / total * 100 for value in pcts]

    def _set_table_col_widths_by_content(self, table, min_pct=8, max_pct=45):
        if not table.rows:
            return
            col_count = max((len(row.cells) for row in ))
            if col_count == 0:
                return
            min_pct = max(1.0, float(min_pct))
            max_pct = max(min_pct, float(max_pct))
            max_weights = [1.0] * col_count
            for row in table.rows:
                for col_idx, cell in enumerate(row.cells):
                    text = "".join((p.text for p in )).strip()
                    if text:
                        max_weights[col_idx] = max(max_weights[col_idx], self._table_text_weight(text))
                else:
                    pcts = self._normalize_table_pcts(max_weights, min_pct, max_pct)
                    tbl = table._tbl
                    tbl_grid = tbl.tblGrid

                if tbl_grid is None:
                    tbl_grid = OxmlElement("w:tblGrid")
                    tbl.insert(0, tbl_grid)

        else:
            for child in list(tbl_grid):
                tbl_grid.remove(child)
            else:
                for pct in pcts:
                    grid_col = OxmlElement("w:gridCol")
                    grid_col.set(qn("w:w"), str(int(pct * 50)))
                    tbl_grid.append(grid_col)
                else:
                    for row in table.rows:
                        for col_idx, cell in enumerate(row.cells):
                            tc = cell._tc
                            tc_pr = tc.tcPr
                            if tc_pr is None:
                                tc_pr = OxmlElement("w:tcPr")
                                tc.insert(0, tc_pr)
                            tc_w = tc_pr.find(qn("w:tcW"))
                            if tc_w is None:
                                tc_w = OxmlElement("w:tcW")
                                tc_pr.append(tc_w)
                            tc_w.set(qn("w:type"), "pct")
                            tc_w.set(qn("w:w"), str(int(pcts[col_idx] * 50)))

    @staticmethod
    def _is_numeric_table_text(text):
        text = (text or "").strip()
        if not text:
            return False
        text = text.replace(",", "").replace("，", "").replace("％", "%")
        text = RE_CURRENCY_PREFIX.sub("", text)
        text = RE_CURRENCY_SUFFIX.sub("", text)
        return RE_NUMERIC_TABLE_TEXT.match(text) is not None

    @staticmethod
    def _is_short_table_text(text, max_len=4):
        text = (text or "").strip()
        return 0 < len(text) <= int(max_len)

    @staticmethod
    def _config_float(config, key, default):
        value = config.get(key, default)
        try:
            if value == "":
                return                 return default
            return float(value)
        except:
            except (TypeError, ValueError):
            return             return default

    def _format_tables(self, doc, apply_color=True):
        if not self.config.get("enable_table_formatting", False):
            self._log("表格自动调整未启用，跳过表格内容格式化。")
            return
            tables = list(doc.tables)
            if not tables:
                self._log("未发现表格，跳过表格内容格式化。")
                return
            table_font = self.config.get("table_font", self.config.get("body_font", "仿宋_GB2312"))
            table_header_font = self.config.get("table_header_font", table_font)
            table_size = self._config_float(self.config, "table_size", self.config.get("body_size", 12))
            table_line_spacing = self._config_float(self.config, "table_line_spacing", 22)
            row_height_cm = self._config_float(self.config, "table_row_height_cm", 0.7)
            border_size_pt = self._config_float(self.config, "table_border_size_pt", 0.5)
            width_percent = self._config_float(self.config, "table_width_percent", 100)
            col_min_pct = self._config_float(self.config, "table_col_min_pct", 8)
            col_max_pct = self._config_float(self.config, "table_col_max_pct", 45)
            short_text_len = self._config_float(self.config, "table_short_text_len", 4)
            auto_col_width = self.config.get("table_auto_col_width", True)
            header_bold = self.config.get("table_header_bold", True)
            smart_align = self.config.get("table_smart_align", False)
            unified_borders = self.config.get("table_unified_borders", True)
            self._log(f"开始格式化表格内容（共 {len(tables)} 个）...")
            for table_idx, table in enumerate(tables, start=1):
                self._log(f"  > 表格 {table_idx}: 调整宽度、行高、字体和单元格格式")
                table.autofit = not auto_col_width
                self._set_table_width_percent(table, width_percent)
                self._set_table_indent(table, 0)
                self._set_table_cell_margins(table)
                if unified_borders:
                    self._set_table_borders(table, size_pt=border_size_pt)
                if auto_col_width:
                    self._set_table_col_widths_by_content(table, min_pct=col_min_pct, max_pct=col_max_pct)

        else:
            serial_col_idx = None
            if table.rows:
                for col_idx, cell in enumerate(table.rows[0].cells):
                    head_text = "".join((p.text for p in )).strip()
                    if not "序号" in head_text:
                        if head_text == "序":
                            pass
                        serial_col_idx = col_idx
                        break

            for row_idx, row in enumerate(table.rows):
                if row_height_cm > 0:
                    row.height = Cm(row_height_cm)
                    row.height_rule = WD_ROW_HEIGHT_RULE.AT_LEAST

        for col_idx, cell in enumerate(row.cells):
            if unified_borders:
                self._set_cell_borders(cell, size_pt=border_size_pt)
            cell_text = "".join((p.text for p in )).strip()
            for para in cell.paragraphs:
                if para.text.strip():
                    for run in para.runs:
                        font_name = table_header_font if row_idx == 0 else table_font
                        self._set_run_font(run, font_name, table_size, set_color=apply_color)
                        if row_idx == 0 and header_bold:
                            run.font.bold = True

                else:
                    para.paragraph_format.first_line_indent = Pt(0)
                    para.paragraph_format.space_before = Pt(0)
                    para.paragraph_format.space_after = Pt(0)
                    if table_line_spacing > 0:
                        para.paragraph_format.line_spacing_rule = WD_LINE_SPACING.EXACTLY
                        para.paragraph_format.line_spacing = Pt(table_line_spacing)
                    else:
                        para.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
                    if smart_align:
                        if row_idx == 0:
                            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        elif "合计" in cell_text or "总计" in cell_text:
                            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        else:
                            if serial_col_idx is not None:
                                if col_idx == serial_col_idx:
                                    para.alignment = WD_ALIGN_PARAGRAPH.CENTER
                            if self._is_numeric_table_text(cell_text):
                                para.alignment = WD_ALIGN_PARAGRAPH.RIGHT
                            elif self._is_short_table_text(cell_text, short_text_len):
                                para.alignment = WD_ALIGN_PARAGRAPH.CENTER
                            else:
                                para.alignment = WD_ALIGN_PARAGRAPH.LEFT

    def _find_title_and_subtitle_paragraphs(self, doc, is_from_txt, start_index=0):
        """
        查找题目和副标题段落的索引范围
        返回: (title_indices, subtitle_indices)
        title_indices: 题目行的索引列表
        subtitle_indices: 副标题行的索引列表
        """
        all_blocks = list(self._iter_block_items(doc))
        first_title_idx = -1
        if is_from_txt:
            self._log("文档源自 TXT，采用智能规则查找题目...")
            for idx in range(start_index, len(all_blocks)):
                block = all_blocks[idx]

            if isinstance(block, Paragraph):
                if block.text.strip():
                    text_to_check = block.text.strip()
                    if RE_TITLE_H1.match(text_to_check) or RE_TITLE_H2.match(text_to_check):
                        self._log(f"  > 首个非空行 (块 {idx + 1}) 符合标题格式，认定本文档无独立题目。")
                        return ([], [])
                self._log(f"  > 在块 {idx + 1} 发现首个非空段落，认定为题目首行。")
                first_title_idx = idx
                break
        else:
            self._log("正在预扫描以确定居中题目位置...")
            for idx in range(start_index, len(all_blocks)):
                block = all_blocks[idx]
                if isinstance(block, Paragraph):
                    if not block.text.strip():
                        pass
                    else:
                        para = block
                        text_to_check = para.text.lstrip()
                        if RE_TITLE_H1.match(text_to_check) or RE_TITLE_H2.match(text_to_check):
                            self._log("  > 发现一级/二级标题，在此之前未找到居中题目。")
                            return ([], [])
                if para.alignment == WD_ALIGN_PARAGRAPH.CENTER:
                    self._log(f"  > 在块 {idx + 1} 发现潜在题目首行。")
                    first_title_idx = idx
                    break
                elif first_title_idx == -1:
                    self._log("  > 扫描结束，未能找到题目。")
                    return ([], [])
                    first_title_para = all_blocks[first_title_idx]
                    title_font, title_size = self._get_paragraph_font_info(first_title_para)
                    title_indices = [
                     first_title_idx]
                    idx = first_title_idx + 1
                    while True:
                        if idx < len(all_blocks):
                            block = all_blocks[idx]
                            if not isinstance(block, Paragraph):
                                break
                            para = block
                            text = para.text.strip()
                            if not text:
                                self._log(f"  > 在块 {idx + 1} 遇到空行，标题识别结束。")
                            else:
                                if para.alignment != WD_ALIGN_PARAGRAPH.CENTER:
                                    break
                            para_font, para_size = self._get_paragraph_font_info(para)
                            if para_font == title_font and para_size == title_size:
                                self._log(f"  > 块 {idx + 1} 也是标题行（居中且字体字号相同）。")
                                title_indices.append(idx)
                                idx += 1

                    break
                else:
                    self._log(f"  > 共识别到 {len(title_indices)} 行标题。")
                    subtitle_indices = []
                    subtitle_start_idx = idx
                    while True:
                        if subtitle_start_idx < len(all_blocks):
                            block = all_blocks[subtitle_start_idx]
                            if isinstance(block, Paragraph):
                                if block.text.strip():
                                    break
                            if isinstance(block, Paragraph):
                                subtitle_start_idx += 1

                    break

    def format_documentParse error at or near `LOAD_FAST' instruction at offset 0


# NOTE: have internal decompilation grammar errors.
# Use -T option to show full context.
# not in loop:
#	break (2)
#      0.  L.1378       168  POP_TOP          
#      1.               170  BREAK_LOOP          174  'to 174'
