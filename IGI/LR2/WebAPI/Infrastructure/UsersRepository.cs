
using MongoDB.Driver;

namespace WebAPI.Infrastructure
{
	public class UsersRepository : IUsersRepository
	{
		public UsersRepository()
		{
			var connectionString = Environment.GetEnvironmentVariable("connectionString") ?? "mongodb://localhost:27017";
			var mongoClient = new MongoClient(connectionString);
			var mongoDatabase = mongoClient.GetDatabase("webApi");
			_users = mongoDatabase.GetCollection<User>("users"); 
		}

		private readonly IMongoCollection<User> _users;
		public async Task AddUser(User user) =>
			await _users.InsertOneAsync(user);

		public async Task DeleteUser(string id) =>
			await _users.FindOneAndDeleteAsync(id);

		public async Task<User> GetUser(string id) =>
			await _users.Find(x => x.Id.ToString() == id).FirstOrDefaultAsync();

		public async Task<IEnumerable<User>> GetUsers() =>
			await _users.Find(_ => true).ToListAsync();

		public async Task UpdateUser(User user) =>
			await _users.FindOneAndReplaceAsync(x => x.Id == user.Id, user);
	}
}
