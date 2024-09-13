import os

# # Set environment variables
# os.environ['DB_SERVER'] = 'ATHENA'
# os.environ['DB_DATABASE'] = 'PythonTestDatabase'
# os.environ['DB_CONNECTION'] = 'trusted_connection=yes'
# Print all environment variables to see if your variables are listed
for key, value in os.environ.items():
    print(f"{key}: {value}")
    