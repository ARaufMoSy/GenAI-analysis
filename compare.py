import google.generativeai as genai

# Setup
API_KEY = "AIzaSyDqGueA1pjjVDXPcoISIzLGNA2CXaPhsKw"
genai.configure(api_key=API_KEY)

# Test prompt
prompt = "Explain the differences between supervised and unsupervised learning"

print("="*60)
print("COMPARING: Flash vs Pro")
print("="*60)

# Test Flash
print("\n1. GEMINI FLASH:")
flash_model = genai.GenerativeModel('gemini-2.5-flash')
flash_response = flash_model.generate_content(prompt)

flash_input = flash_response.usage_metadata.prompt_token_count
flash_output = flash_response.usage_metadata.candidates_token_count
flash_cost = (flash_input/1_000_000 * 0.075) + (flash_output/1_000_000 * 0.30)

print(f"Input tokens:  {flash_input}")
print(f"Output tokens: {flash_output}")
print(f"Cost: ${flash_cost:.6f}")

# Test Pro
print("\n2. GEMINI PRO:")
pro_model = genai.GenerativeModel('gemini-2.5-pro')
pro_response = pro_model.generate_content(prompt)

pro_input = pro_response.usage_metadata.prompt_token_count
pro_output = pro_response.usage_metadata.candidates_token_count
pro_cost = (pro_input/1_000_000 * 1.25) + (pro_output/1_000_000 * 5.00)

print(f"Input tokens:  {pro_input}")
print(f"Output tokens: {pro_output}")
print(f"Cost: ${pro_cost:.6f}")

# Compare
print("\n" + "="*60)
print("COMPARISON:")
print(f"Pro is {pro_cost/flash_cost:.1f}x more expensive")
print(f"Difference: ${pro_cost - flash_cost:.6f} per request")

# Business scale
print(f"\nFor 1000 requests/day:")
print(f"Flash: ${flash_cost * 1000:.2f}/day = ${flash_cost * 30000:.2f}/month")
print(f"Pro:   ${pro_cost * 1000:.2f}/day = ${pro_cost * 30000:.2f}/month")
print(f"Savings: ${(pro_cost - flash_cost) * 30000:.2f}/month with Flash")