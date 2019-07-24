IPY=python -c
.PHONY:
	hello
	err

hello:
	# this is a comment followed by a multi-line command
	$(IPY) \
    "print('hello world')"

err:
	keyboardmashitalltogetherthisshouldnotrunotherwiseunittestswillfail

circle:
	# of life
	circle

empty:
	# head

commented_var:
    # this should not harm: $(dummy)

one:
	@make two

two:
	@+make empty
	@+make three

three:
	@+make circle
