import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common';

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
  imports: [RouterOutlet, CommonModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})

export class AppComponent {
  title = 'frontend';
  data: IProcessamento[] = [];

  async getListProcessamento() {
    try {
      const response = await fetch('http://localhost:8000/api/processamento', {
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

  async processamento() {
    try {
      const response = await fetch('http://localhost:8000/api/processamento', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
      });
  
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
  
      this.data = await response.json();
    } catch(error) {
      console.error('Erro ao processar os dados:', error);
    }
  }

  ngOnInit() {
    this.getListProcessamento();
  }
}
