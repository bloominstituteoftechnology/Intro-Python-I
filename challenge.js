random = [ 'Joe', '2', 'Ted', '4.98', '14', 'Sam', 'void *', '42', 'float', 'pointers', '5006' ];

// random.forEach((e) => {
// 	return console.log(e);
// });

const printEach = (value) => {
	random2 = [
		'Bob',
		'Slack',
		[ 'reddit', '89', 101, [ 'alacritty', '(brackets)', 5, 375 ] ],
		0,
		[ '{slice, owned}' ],
		22
	];
	if ((value = Array)) {
		value.forEach((item) => {
			return console.log(item);
		});
	}
};

printEach(random);
