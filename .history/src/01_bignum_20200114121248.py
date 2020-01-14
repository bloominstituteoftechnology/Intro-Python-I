# Print out 2 to the 65536 power
# (try doing the same thing in the JS console and see what it outputs)

# YOUR CODE HERE
const db = require(dbConfig);

module.exports = {
  findAll,
  findById,
  remove,
  register,
  editById,
  findByUserName
};

const table = 'admin';
function findAll() {
  return db(table);
}

function findById(id) {
  id = Array.isArray(id) ? [id] : id;
  return db(table)
    .where({ id })
    .first()
    .then(res => console.log(res))
    .catch(res => console.log(res));
}

function findByUserName(admin) {
  if (admin.username) {
    const username = admin.username;
    return db(table)
      .where({ username })
      .first();
  }
}

function remove(id) {
  return db(table)
    .where({ id })
    .del();
}
function editById(id, update) {
  return db(table)
    .where({ id })
    .update(update, '*');
}
function register(obj) {
  return db(table)
    .insert(obj)
    .then(([id]) => findById(id));
}
