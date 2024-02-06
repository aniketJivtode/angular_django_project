import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SharedService {
  // [x: string]: any;
  readonly APIUrl = 'http://127.0.0.1:8000';
  // readonly PhotoUrl = 'http://127.0.0.1:8000/media'
  
  // const httpOptions = {
  //   headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  // };
  

  constructor(private http:HttpClient) {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
   }

  getProfileList():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/api/v1/user/profiles/');
  }

  addUserProfile(val:any){
    return this.http.post(this.APIUrl + '/api/v1/user/profiles/',val);
  }

  updateUserProfile(val:any): Observable<any>{
    console.log('data of updateprofile',val)
    return this.http.post(this.APIUrl + '/api/v1/user/profiles/',val);
  }

  deleteProfile(val:any){
    return this.http.delete(this.APIUrl + '/api/v1/user/profiles/'+val);
  }
  // UploadPhoto(val:any){
  //   return this.http.post(this.APIUrl+'/saveFile',val);
  // }
  getAllProfileName():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl+'/profiles/');
  }
}
