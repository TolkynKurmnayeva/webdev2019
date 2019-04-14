import { EventEmitter, Injectable } from '@angular/core';
import { MainService } from '../services/main.service';
import { HttpClient } from '@angular/common/http';
import { TaskList , Task } from '../models/models';


@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  constructor(http: HttpClient) {
    super(http);
  }

  getTaskLists(): Promise<any> {
    return this.http.get('http://localhost:8000/task_list/', {}).toPromise().then(res => res);
  }
  getTasks(taskList: TaskList): Promise<any> {
    return this.http.get('http://localhost:8000/task_list/' + taskList.id + '/tasks', {}).toPromise().then(res1 => res1);
  }
}
