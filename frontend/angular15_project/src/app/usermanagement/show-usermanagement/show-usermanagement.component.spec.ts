import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShowUsermanagementComponent } from './show-usermanagement.component';

describe('ShowUsermanagementComponent', () => {
  let component: ShowUsermanagementComponent;
  let fixture: ComponentFixture<ShowUsermanagementComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ShowUsermanagementComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ShowUsermanagementComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
