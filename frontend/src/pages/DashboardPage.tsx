import { useAuthStore } from '../store/authStore'

export default function DashboardPage() {
  const { user } = useAuthStore()

  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">Dashboard</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
        <div className="card">
          <h3 className="text-lg font-semibold mb-2">Welcome!</h3>
          <p className="text-gray-600">
            {user?.first_name} {user?.last_name}
          </p>
        </div>
        
        <div className="card">
          <h3 className="text-lg font-semibold mb-2">Projects</h3>
          <p className="text-3xl font-bold text-primary-600">0</p>
          <p className="text-sm text-gray-500">Active projects</p>
        </div>
        
        <div className="card">
          <h3 className="text-lg font-semibold mb-2">Team Members</h3>
          <p className="text-3xl font-bold text-primary-600">0</p>
          <p className="text-sm text-gray-500">Total members</p>
        </div>
      </div>

      <div className="card">
        <h2 className="text-xl font-semibold mb-4">User Information</h2>
        <div className="space-y-2">
          <div className="flex justify-between">
            <span className="text-gray-600">Mobile:</span>
            <span className="font-medium">{user?.mobile}</span>
          </div>
          <div className="flex justify-between">
            <span className="text-gray-600">National Code:</span>
            <span className="font-medium">{user?.national_code}</span>
          </div>
          <div className="flex justify-between">
            <span className="text-gray-600">Status:</span>
            <span className={`font-medium ${user?.is_active ? 'text-green-600' : 'text-red-600'}`}>
              {user?.is_active ? 'Active' : 'Inactive'}
            </span>
          </div>
        </div>
      </div>

      <div className="mt-8 card">
        <h2 className="text-xl font-semibold mb-4">Coming Soon</h2>
        <p className="text-gray-600">
          Project management, team assignment, and real-time monitoring features will be available soon.
        </p>
      </div>
    </div>
  )
}

