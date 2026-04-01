// Общие типы данных между Frontend и Backend

export interface HealthResponse {
  status: string;
  timestamp: string;
  service: string;
}

export interface User {
  id: number;
  username: string;
  email: string;
}

export interface ApiResponse<T> {
  success: boolean;
  data?: T;
  error?: string;
}
