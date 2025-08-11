import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';  // Import HttpClientModule here
import { AuthService } from '../../../services/auth';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [CommonModule, FormsModule, ReactiveFormsModule, HttpClientModule],  // Add HttpClientModule here
  templateUrl: './register.html',
  styleUrls: ['./register.scss']
})
export class Register {
  fullname = '';
  email = '';
  password = '';
  confirmPassword = '';
  errorMessage = '';

  constructor(private authService: AuthService, private router: Router) {}

  onSubmit() {
    if (this.password !== this.confirmPassword) {
      this.errorMessage = 'Passwords do not match';
      return;
    }
    this.authService.register(this.email, this.password, this.fullname).subscribe({
      next: () => this.router.navigate(['/auth/login']),
      error: err => this.errorMessage = err.error?.detail || 'Registration failed'
    });
  }
}
