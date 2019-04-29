import { EventEmitter, Injectable } from '@angular/core';
import { MainService } from '../services/main.service';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { TaskList , Task, IAuthResponse } from '../models/models';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  baseurl = "http://127.0.0.1:8000";
  httpHeaders = new HttpHeaders({'Content-Type' : 'application/json'})
  constructor(http: HttpClient) {
    super(http);
  
  }

  getAllTaskLists(): Observable<any>{
    return this.http.get(this.baseurl + '/api/task_list/',
    {headers: this.httpHeaders});
  }


  updateTasklist(tasklist): Observable<any> {
    const body = {id: tasklist.id , name: tasklist.name };
    return this.http.put(this.baseurl + '/api/task_list/' + tasklist.id + '/', body,
    {headers: this.httpHeaders});
  }

  createTasklist(tasklist): Observable<any> {
    const body = {id: tasklist.id , name: tasklist.name};
    return this.http.post(this.baseurl + '/api/task_list/', body,
    {headers: this.httpHeaders});
  }

  deleteTasklist(id): Observable<any> {
    return this.http.delete(this.baseurl + '/api/task_list/' + id + '/',
    {headers: this.httpHeaders});
  }

  auth(login: string, password: string): Promise<IAuthResponse> {
    return this.post('http://localhost:8000/api/login/', {
      username: login,
      password: password
    });
  }

  logout(): Promise<any> {
    return this.post('http://localhost:8000/api/logout/', {});
  }

}
