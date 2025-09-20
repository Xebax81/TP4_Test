import { render, screen, fireEvent } from '@testing-library/react';
import App from './App';

describe('Calculadora App', () => {
  test('renders calculator title', () => {
    render(<App />);
    const titleElement = screen.getByText(/🧮 Calculadora TP7/i);
    expect(titleElement).toBeInTheDocument();
  });

  test('renders initial display value', () => {
    render(<App />);
    const displayElement = screen.getByText('0');
    expect(displayElement).toBeInTheDocument();
  });

  test('can input numbers', () => {
    render(<App />);
    
    const button5 = screen.getByText('5');
    fireEvent.click(button5);
    
    const displayElement = screen.getByText('5');
    expect(displayElement).toBeInTheDocument();
  });

  test('can perform addition', () => {
    render(<App />);
    
    // Click 2 + 3 =
    fireEvent.click(screen.getByText('2'));
    fireEvent.click(screen.getByText('+'));
    fireEvent.click(screen.getByText('3'));
    fireEvent.click(screen.getByText('='));
    
    const displayElement = screen.getByText('5');
    expect(displayElement).toBeInTheDocument();
  });

  test('can perform subtraction', () => {
    render(<App />);
    
    // Click 8 - 3 =
    fireEvent.click(screen.getByText('8'));
    fireEvent.click(screen.getByText('-'));
    fireEvent.click(screen.getByText('3'));
    fireEvent.click(screen.getByText('='));
    
    const displayElement = screen.getByText('5');
    expect(displayElement).toBeInTheDocument();
  });

  test('can perform multiplication', () => {
    render(<App />);
    
    // Click 4 × 3 =
    fireEvent.click(screen.getByText('4'));
    fireEvent.click(screen.getByText('×'));
    fireEvent.click(screen.getByText('3'));
    fireEvent.click(screen.getByText('='));
    
    const displayElement = screen.getByText('12');
    expect(displayElement).toBeInTheDocument();
  });

  test('can perform division', () => {
    render(<App />);
    
    // Click 9 ÷ 3 =
    fireEvent.click(screen.getByText('9'));
    fireEvent.click(screen.getByText('÷'));
    fireEvent.click(screen.getByText('3'));
    fireEvent.click(screen.getByText('='));
    
    const displayElement = screen.getByText('3');
    expect(displayElement).toBeInTheDocument();
  });

  test('clear button resets calculator', () => {
    render(<App />);
    
    // Input some numbers and operation
    fireEvent.click(screen.getByText('5'));
    fireEvent.click(screen.getByText('+'));
    fireEvent.click(screen.getByText('3'));
    
    // Click clear
    fireEvent.click(screen.getByText('AC'));
    
    const displayElement = screen.getByText('0');
    expect(displayElement).toBeInTheDocument();
  });

  test('handles division by zero', () => {
    render(<App />);
    
    // Click 5 ÷ 0 =
    fireEvent.click(screen.getByText('5'));
    fireEvent.click(screen.getByText('÷'));
    fireEvent.click(screen.getByText('0'));
    fireEvent.click(screen.getByText('='));
    
    const displayElement = screen.getByText('0');
    expect(displayElement).toBeInTheDocument();
  });

  test('renders pipeline status information', () => {
    render(<App />);
    
    const statusElement = screen.getByText(/✅ Deployed Successfully/i);
    expect(statusElement).toBeInTheDocument();
    
    const environmentElement = screen.getByText(/Development/i);
    expect(environmentElement).toBeInTheDocument();
  });

  test('renders features list', () => {
    render(<App />);
    
    const featuresTitle = screen.getByText(/📋 Features Implementadas/i);
    expect(featuresTitle).toBeInTheDocument();
    
    const basicOperations = screen.getByText(/✅ Operaciones básicas/i);
    expect(basicOperations).toBeInTheDocument();
    
    const pipeline = screen.getByText(/✅ Pipeline automático en PR/i);
    expect(pipeline).toBeInTheDocument();
  });
});