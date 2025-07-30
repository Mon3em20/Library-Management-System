from supabase import create_client, Client
import os;

url = "https://ovxashdjihyrnuodmvur.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im92eGFzaGRqaWh5cm51b2RtdnVyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTM4NjkwOTEsImV4cCI6MjA2OTQ0NTA5MX0.JBkeJ7uYWYAEgPCWiprenooU5z5qlKYEKXQTGC4DsfY"

supabase: Client = create_client(url, key)