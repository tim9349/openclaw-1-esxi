
import sys
import os

# Add the directory containing taifex.py to the Python path
sys.path.append('/home/dm/QAPI_DM_Quote')

try:
    from taifex import fetch_foreign_position, fetch_large_traders
    
    print("--- Testing fetch_foreign_position ---")
    foreign_data = fetch_foreign_position()
    print(f"Foreign Position Data: {foreign_data}")

    print("\n--- Testing fetch_large_traders ---")
    large_trader_data = fetch_large_traders()
    print(f"Large Trader Data: {large_trader_data}")

except Exception as e:
    print(f"Error during execution: {e}")
