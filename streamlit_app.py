// App.js simplificada para web
import React, { useState } from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';

export default function App() {
  const [signal, setSignal] = useState(null);
  
  const analyzeCrypto = async () => {
    // Simulación de análisis de BTC
    setSignal({
      symbol: "BTC/USDT",
      recommendation: "COMPRA",
      confidence: "85%",
      reason: "RSI en zona de sobreventa y cruce alcista en MACD",
      target: "$65,000",
      stoploss: "$61,200"
    });
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>AI Trading Demo</Text>
      
      <Button title="Analizar BTC/USDT" onPress={analyzeCrypto} />
      
      {signal && (
        <View style={styles.card}>
          <Text style={styles.symbol}>{signal.symbol}</Text>
          <Text style={signal.recommendation === "COMPRA" ? 
                        styles.buy : styles.sell}>
            {signal.recommendation}
          </Text>
          <Text>Confianza: {signal.confidence}</Text>
          <Text>Razón: {signal.reason}</Text>
          <Text>Objetivo: {signal.target}</Text>
          <Text>Stop Loss: {signal.stoploss}</Text>
        </View>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#f0f2f5'
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20
  },
  card: {
    backgroundColor: 'white',
    padding: 15,
    borderRadius: 10,
    marginTop: 20,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 6,
    elevation: 3
  },
  symbol: {
    fontSize: 18,
    fontWeight: 'bold'
  },
  buy: {
    color: 'green',
    fontSize: 22,
    fontWeight: 'bold',
    marginVertical: 10
  },
  sell: {
    color: 'red',
    fontSize: 22,
    fontWeight: 'bold',
    marginVertical: 10
  }
});
