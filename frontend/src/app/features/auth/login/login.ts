import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router, RouterLink } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { AuthService, TokenResponse } from '../../../services/auth';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, FormsModule,RouterLink],
  templateUrl: './login.html',
  styleUrls: ['./login.scss']
})
export class Login {
  username = '';
  password = '';
  errorMessage = '';
  token: TokenResponse | null = null;

  constructor(private authService: AuthService, private router: Router) {}

onSubmit() {
  this.errorMessage = '';
  this.token = null;

  this.authService.login(this.username, this.password).subscribe({
    next: (res) => {
      this.token = res;
      localStorage.setItem('access_token', res.access_token);
      localStorage.setItem('username', this.username);
      this.router.navigate(['/home']);  // Navigate to home on success
    },
    error: (err) => {
      this.errorMessage = err.error?.detail || 'Login failed';
    }
  });
}

}
