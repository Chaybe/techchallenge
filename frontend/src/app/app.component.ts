import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms'

interface IProcessamento {
  id:number,
  num1:number,
  num2:number
  num3:number
  status:string,
  media:number,
  mediana:number
}

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, CommonModule, FormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})

export class AppComponent {
  num1 = 0;
  num2 = 0;
  num3 = 0;

  title = 'frontend';
  data: IProcessamento[] = [];
  baseUrl = 'http://localhost:8000/api';
  
  private konamiCode: string[] = [
    'ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown',
    'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight',
    'b', 'a'
  ];
  private konamiIndex = 0;

  async getListProcessamento() {
    try {
      const response = await fetch(`${this.baseUrl}/processamento`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });
  
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
  
      this.data = await response.json();
    } catch (error) {
      console.error('Erro ao buscar os dados:', error);
    }
  }

  async createProcessamento() {
    const body = {
      num1: this.num1,
      num2: this.num2,
      num3: this.num3
    };

    try {
      const response = await fetch(`${this.baseUrl}/processamento`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(body), 
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const result = await response.json();

      this.getListProcessamento();
    } catch (error) {
      console.error('Erro ao salvar os dados:', error);
    }
  }

  detect_KC() {
    // Exec: up up down down left right left right b a
    
    window.addEventListener('keydown', (event) => {
      if (event.key === this.konamiCode[this.konamiIndex]) {
        this.konamiIndex++;
        if (this.konamiIndex === this.konamiCode.length) {
          window.open(atob('aHR0cHM6Ly95b3V0dS5iZS9HQklJUTBrUDE1RT9zaT1vdHZiUk5fT0pGV0lkZU5P'), '_blank');
          this.konamiIndex = 0; 
        }
      } else {
        this.konamiIndex = 0;
      }
    });
  }

  ngOnInit() {
    this.getListProcessamento();
    this.detect_KC();
  }
}
