import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useMutation } from '@tanstack/react-query'
import { authApi } from '../api/auth'
import type { SignupRequest, SignupVerifyOTP } from '../types'

export default function SignupPage() {
  const navigate = useNavigate()
  const [step, setStep] = useState<'request' | 'verify'>('request')
  const [signupKey, setSignupKey] = useState<string>('')
  const [formData, setFormData] = useState<SignupRequest>({
    mobile: '',
    password: '',
    national_code: '',
    birthday_jalali: '',
  })
  const [otp, setOtp] = useState('')

  // Request OTP mutation
  const requestOtpMutation = useMutation({
    mutationFn: (data: SignupRequest) => authApi.signupRequest(data),
    onSuccess: (response) => {
      setSignupKey(response.key)
      setStep('verify')
    },
    onError: (error: any) => {
      alert(error.response?.data?.detail || 'Signup failed. Please try again.')
    },
  })

  // Verify OTP mutation
  const verifyOtpMutation = useMutation({
    mutationFn: (data: SignupVerifyOTP) => authApi.signupVerify(data),
    onSuccess: () => {
      navigate('/dashboard')
    },
    onError: (error: any) => {
      alert(error.response?.data?.detail || 'OTP verification failed.')
    },
  })

  const handleRequestSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    requestOtpMutation.mutate(formData)
  }

  const handleVerifySubmit = (e: React.FormEvent) => {
    e.preventDefault()
    verifyOtpMutation.mutate({ key: signupKey, otp })
  }

  if (step === 'verify') {
    return (
      <div className="max-w-md mx-auto">
        <div className="card">
          <h2 className="text-2xl font-bold mb-6">Verify OTP</h2>
          <p className="text-gray-600 mb-4">
            We've sent an OTP to your mobile number. Please enter it below.
          </p>
          <form onSubmit={handleVerifySubmit} className="space-y-4">
            <div>
              <label htmlFor="otp" className="block text-sm font-medium text-gray-700 mb-2">
                OTP Code
              </label>
              <input
                id="otp"
                type="text"
                value={otp}
                onChange={(e) => setOtp(e.target.value)}
                className="input"
                placeholder="Enter 6-digit OTP"
                maxLength={6}
                required
              />
            </div>
            <button
              type="submit"
              disabled={verifyOtpMutation.isPending}
              className="btn btn-primary w-full"
            >
              {verifyOtpMutation.isPending ? 'Verifying...' : 'Verify OTP'}
            </button>
            <button
              type="button"
              onClick={() => setStep('request')}
              className="btn btn-secondary w-full"
            >
              Back
            </button>
          </form>
        </div>
      </div>
    )
  }

  return (
    <div className="max-w-md mx-auto">
      <div className="card">
        <h2 className="text-2xl font-bold mb-6">Create Account</h2>
        <form onSubmit={handleRequestSubmit} className="space-y-4">
          <div>
            <label htmlFor="mobile" className="block text-sm font-medium text-gray-700 mb-2">
              Mobile Number
            </label>
            <input
              id="mobile"
              type="tel"
              value={formData.mobile}
              onChange={(e) => setFormData({ ...formData, mobile: e.target.value })}
              className="input"
              placeholder="09123456789"
              required
            />
          </div>

          <div>
            <label htmlFor="password" className="block text-sm font-medium text-gray-700 mb-2">
              Password
            </label>
            <input
              id="password"
              type="password"
              value={formData.password}
              onChange={(e) => setFormData({ ...formData, password: e.target.value })}
              className="input"
              placeholder="Enter your password"
              required
              minLength={6}
            />
          </div>

          <div>
            <label htmlFor="national_code" className="block text-sm font-medium text-gray-700 mb-2">
              National Code
            </label>
            <input
              id="national_code"
              type="text"
              value={formData.national_code}
              onChange={(e) => setFormData({ ...formData, national_code: e.target.value })}
              className="input"
              placeholder="10-digit national code"
              maxLength={10}
              required
            />
          </div>

          <div>
            <label htmlFor="birthday_jalali" className="block text-sm font-medium text-gray-700 mb-2">
              Birthday (Jalali)
            </label>
            <input
              id="birthday_jalali"
              type="text"
              value={formData.birthday_jalali}
              onChange={(e) => setFormData({ ...formData, birthday_jalali: e.target.value })}
              className="input"
              placeholder="1371/01/01"
              required
            />
            <p className="text-xs text-gray-500 mt-1">Format: YYYY/MM/DD (Jalali calendar)</p>
          </div>

          <button
            type="submit"
            disabled={requestOtpMutation.isPending}
            className="btn btn-primary w-full"
          >
            {requestOtpMutation.isPending ? 'Sending OTP...' : 'Sign Up'}
          </button>
        </form>
      </div>
    </div>
  )
}

