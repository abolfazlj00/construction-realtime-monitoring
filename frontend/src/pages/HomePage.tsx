import { Link } from 'react-router-dom'
import { useAuthStore } from '../store/authStore'

export default function HomePage() {
  const { isAuthenticated } = useAuthStore()

  return (
    <div className="text-center">
      <h1 className="text-4xl font-bold text-gray-900 mb-4">
        Construction Realtime Monitoring
      </h1>
      <p className="text-xl text-gray-600 mb-8">
        Track your construction projects in real-time with instant insights and better project control.
      </p>

      {isAuthenticated ? (
        <Link to="/dashboard" className="btn btn-primary text-lg px-8 py-3">
          Go to Dashboard
        </Link>
      ) : (
        <div className="flex justify-center space-x-4">
          <Link to="/signup" className="btn btn-primary text-lg px-8 py-3">
            Get Started
          </Link>
          <Link to="/login" className="btn btn-secondary text-lg px-8 py-3">
            Login
          </Link>
        </div>
      )}

      <div className="mt-16 grid grid-cols-1 md:grid-cols-3 gap-8">
        <div className="card">
          <h3 className="text-xl font-semibold mb-2">Real-time Tracking</h3>
          <p className="text-gray-600">
            Monitor your construction projects with live updates and instant notifications.
          </p>
        </div>
        <div className="card">
          <h3 className="text-xl font-semibold mb-2">Team Management</h3>
          <p className="text-gray-600">
            Assign roles, manage team members, and track on-site status instantly.
          </p>
        </div>
        <div className="card">
          <h3 className="text-xl font-semibold mb-2">Project Control</h3>
          <p className="text-gray-600">
            Get accurate live insights for better project control and decision making.
          </p>
        </div>
      </div>
    </div>
  )
}

