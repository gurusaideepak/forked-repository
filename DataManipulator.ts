import { ServerRespond } from './DataStreamer';

export interface Row {
  price_abc: number,
  price_def: number,
  ratio: number,
  timestamp: Date,
  upper_bound: number,
  lower_bound: number,
  trigger_alert:number | undefind,
}


export class DataManipulator {
  static generateRow(serverResponds: ServerRespond[]): Row {
    const priceABC = (severRespond[0].top_ask.price + serverRespond[0].top_bid_price) / 2;
    const priceDEF = (severRespond[1].top_ask.price + serverRespond[1].top_bid_price) / 2;
    const ratio = priceABC / priceDEF;
    const upperBound = 1 + 0.5;
    const lowerBound = 1 - 0.5;
    return {
      price_abc: priceABC,
      price_def: priceDEF,
      ratio,
      timestamp: severRespond[0].timestamp > severRespond[1].timestamp ?
        severRespond[0].timestamp : severRespond[1].timestamp,
      upper_bound: upperBound,
      lower_bound: lowerBound,
      trigger_alert: (ratio > upperBound || ratio < lowerBound) ? ratio : undefined,
      };
    }
  }
}
