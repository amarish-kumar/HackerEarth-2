-module(modulo_sorting).
-export([main/0]).

lc_quicksort([], _) -> [];
lc_quicksort([Pivot|Rest], K) ->
	lc_quicksort([Smaller || Smaller <- Rest, Smaller rem K < Pivot rem K], K)
	++ [Pivot] ++
	lc_quicksort([Larger || Larger <- Rest, Larger rem K >= Pivot rem K], K).

print_list([A]) -> io:format("~p", [A]);
print_list([H|T]) ->
	io:format("~p ", [H]),
	print_list(T).

modulo_sort(A, K) ->
	SortedA = lc_quicksort(A, K),
	print_list(SortedA)
	.

main() ->
	{ok, [_,K]} = io:fread("", "~d ~d"),
	S = string:strip(io:get_line(""),both,$\n),
	A = [X || {X,_} <- [string:to_integer(Z) || Z <- string:tokens(S," ")]],
	modulo_sort(A, K)
	.
