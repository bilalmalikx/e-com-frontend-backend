import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ForgetPassowrd } from './forget-passowrd';

describe('ForgetPassowrd', () => {
  let component: ForgetPassowrd;
  let fixture: ComponentFixture<ForgetPassowrd>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ForgetPassowrd]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ForgetPassowrd);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
