import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

type Number = int | float
type Numbers = list[Number]

def open_dataset(dataset_filename) -> pd.DataFrame:
    return pd.read_csv(f'../datasets/{dataset_filename}')
    
def net_profit(cost_savings: Number, total_investment: Number, display: bool=True) -> Number:
    np = cost_savings - total_investment
    
    if display:
        print(f'Estimated net_profit: {np}')
        
    return np
    
def return_on_investment(net_profit: Number, total_cost: Number, decimals: int=1, display: bool=True) -> Number:
    roi = round((net_profit / total_cost) * 100, decimals)
    
    if display:
        print(f'Return on Investment: {roi}')
        
    return roi
    
def get_roi_figs(cost_savings_scenarios: Numbers, total_sums: Number, display: bool=False) -> tuple[Numbers, Numbers]:
    nets = [net_profit(cs, total_sums) for cs in cost_savings_scenarios]
    rois = [return_on_investment(net, total_sums) for net in nets]

    if display:
        for idx, cs in enumerate(cost_savings_scenarios):
            print(f'For scenario {idx}, or a cost savings of {cs}, here are the following:\n\tNet profit\t{nets[idx]}\n\tROI:\t{rois[idx]}')
        
    return nets, rois

def project_acceptance(roi: Number, threshold: Number) -> bool:
    return roi >= threshold