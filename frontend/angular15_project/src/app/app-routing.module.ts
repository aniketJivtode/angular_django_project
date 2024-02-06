import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UsermanagementComponent } from './usermanagement/usermanagement.component';

const routes: Routes = [
  {path: "profile",component:UsermanagementComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
