from trie_dict import create_trie_node, add_word, is_word, num_completions, get_completions

t = create_trie_node()
add_word("a", t)
add_word("an", t) 
add_word("and", t)
add_word("ant", t)
add_word("ants", t)
add_word("andy", t)
#print("THE TRIE", t)
add_word("are", t) 
add_word("be", t)
add_word("bet", t)
add_word("bee", t)
add_word("beet", t)
add_word("beer", t)
add_word("beers", t)

#print(t)
# Write your tests here

# Example of an assertion. If "bee" was not inserted
# correctly in the trie, the following statement will
# cause the program to exit with an error message.
#assert is_word("bee", t)

#print(is_word("ar", t))

rv1 = get_completions("an", t)
rv2 = get_completions("bee", t)
rv3 = get_completions("as", t)
rv4 = get_completions("and", t)
#print(rv1, rv2, rv3)
#print(rv4)


num1 = num_completions("an", t)
num2 = num_completions("be", t)
num3 = num_completions("beer", t)
num4 = num_completions("bat", t)

#print("an ", "expected = 5 ", "actual = ", num1)
#print("be ", "expected = 6 ", "actual = ", num2)
#print("beer ", "expected = 2 ", "actual = ", num3)
#print("bat ", "expected = 'Prefix not in dictionary'", "actual = ", num4)


