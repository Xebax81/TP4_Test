import React, { useState } from 'react';
import './App.css';

function App() {
  const [display, setDisplay] = useState('0');
  const [previousValue, setPreviousValue] = useState(null);
  const [operation, setOperation] = useState(null);
  const [waitingForNewValue, setWaitingForNewValue] = useState(false);

  const inputNumber = (num) => {
    if (waitingForNewValue) {
      setDisplay(String(num));
      setWaitingForNewValue(false);
    } else {
      setDisplay(display === '0' ? String(num) : display + num);
    }
  };

  const inputOperation = (nextOperation) => {
    const inputValue = parseFloat(display);

    if (previousValue === null) {
      setPreviousValue(inputValue);
    } else if (operation) {
      const currentValue = previousValue || 0;
      const newValue = calculate(currentValue, inputValue, operation);

      setDisplay(String(newValue));
      setPreviousValue(newValue);
    }

    setWaitingForNewValue(true);
    setOperation(nextOperation);
  };

  const calculate = (firstValue, secondValue, operation) => {
    switch (operation) {
      case '+':
        return firstValue + secondValue;
      case '-':
        return firstValue - secondValue;
      case '*':
        return firstValue * secondValue;
      case '/':
        return secondValue !== 0 ? firstValue / secondValue : 0;
      case '=':
        return secondValue;
      default:
        return secondValue;
    }
  };

  const performCalculation = () => {
    const inputValue = parseFloat(display);

    if (previousValue !== null && operation) {
      const newValue = calculate(previousValue, inputValue, operation);
      setDisplay(String(newValue));
      setPreviousValue(null);
      setOperation(null);
      setWaitingForNewValue(true);
    }
  };

  const clearDisplay = () => {
    setDisplay('0');
    setPreviousValue(null);
    setOperation(null);
    setWaitingForNewValue(false);
  };

  const Button = ({ onClick, className = '', children }) => (
    <button className={`button ${className}`} onClick={onClick}>
      {children}
    </button>
  );

  return (
    <div className="App">
      <header className="App-header">
        <h1>🧮 Calculadora TP7</h1>
        <p>Ingeniería de Software - CI/CD Pipeline Demo</p>
      </header>
      
      <div className="calculator">
        <div className="display">
          <div className="display-value">{display}</div>
        </div>
        
        <div className="buttons">
          <Button onClick={clearDisplay} className="button-clear">
            AC
          </Button>
          <Button onClick={() => inputOperation('/')} className="button-operator">
            ÷
          </Button>
          <Button onClick={() => inputOperation('*')} className="button-operator">
            ×
          </Button>
          <Button onClick={() => inputOperation('-')} className="button-operator">
            -
          </Button>

          <Button onClick={() => inputNumber(7)}>7</Button>
          <Button onClick={() => inputNumber(8)}>8</Button>
          <Button onClick={() => inputNumber(9)}>9</Button>
          <Button onClick={() => inputOperation('+')} className="button-operator">
            +
          </Button>

          <Button onClick={() => inputNumber(4)}>4</Button>
          <Button onClick={() => inputNumber(5)}>5</Button>
          <Button onClick={() => inputNumber(6)}>6</Button>

          <Button onClick={() => inputNumber(1)}>1</Button>
          <Button onClick={() => inputNumber(2)}>2</Button>
          <Button onClick={() => inputNumber(3)}>3</Button>
          <Button onClick={performCalculation} className="button-equals">
            =
          </Button>

          <Button onClick={() => inputNumber(0)} className="button-zero">
            0
          </Button>
          <Button onClick={() => setDisplay(display + '.')}>.</Button>
        </div>
      </div>

      <footer className="App-footer">
        <div className="pipeline-info">
          <h3>🚀 Pipeline CI/CD Status</h3>
          <div className="status-badge success">✅ Deployed Successfully</div>
          <p>Environment: <strong>Development</strong></p>
          <p>Version: <strong>1.0.0</strong></p>
          <p>Last Deploy: <strong>{new Date().toLocaleString()}</strong></p>
        </div>
        
        <div className="features">
          <h3>📋 Features Implementadas</h3>
          <ul>
            <li>✅ Operaciones básicas (+, -, ×, ÷)</li>
            <li>✅ Pipeline automático en PR</li>
            <li>✅ Deploy a Firebase Hosting</li>
            <li>✅ Pruebas automatizadas</li>
            <li>✅ Análisis de calidad</li>
            <li>✅ HOTFIX pipeline</li>
          </ul>
        </div>
      </footer>
    </div>
  );
}

export default App;