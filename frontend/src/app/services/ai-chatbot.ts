import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class AIChatbotService {
  private baseUrl = '/api/ai';

  constructor(private http: HttpClient) {}

  queryAI(query: string): Observable<any> {
    return this.http.post(`${this.baseUrl}/query`, { query });
  }
}
