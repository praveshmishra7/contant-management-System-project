# Contact Management System
# Week 3 Project - Functions & Dictionaries

import json
import re
from datetime import datetime, timedelta
import csv
import os

DATA_FILE = "contacts_data.json"
CSV_EXPORT_FILE = "contacts_export.csv"


def validate_phone(phone: str):
    """Validate phone number format. Returns (is_valid, cleaned_digits_or_none)."""
    digits = re.sub(r"\D", "", phone)
    if 10 <= len(digits) <= 15:
        return True, digits
    return False, None


def validate_email(email: str):
    """Validate email format."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

def load_contacts():
    """Load contacts from DATA_FILE."""
    if not os.path.exists(DATA_FILE):
        return {}

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Expect: {"Name": {..contact..}, ...}
            if isinstance(data, dict):
                return data
    except (json.JSONDecodeError, OSError):
        pass

    return {}


def save_contacts(contacts: dict):
    """Save contacts to DATA_FILE."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=4)


def add_contact(contacts: dict):
    """Add a new contact to the dictionary."""
    print("\n--- ADD NEW CONTACT ---")

    # Get contact name
    while True:
        name = input("Enter contact name: ").strip()
        if not name:
            print("Name cannot be empty!")
            continue

        if name in contacts:
            print(f"Contact '{name}' already exists!")
            choice = input("Do you want to update instead? (y/n): ").lower()
            if choice == "y":
                update_contact(contacts, name)
            return contacts

        break

    # Get phone number with validation
    while True:
        phone = input("Enter phone number: ").strip()
        is_valid, cleaned_phone = validate_phone(phone)
        if is_valid:
            break
        print("Invalid phone number! Please enter 10-15 digits.")

    # Get email with validation
    while True:
        email = input("Enter email (optional, press Enter to skip): ").strip()
        if not email:
            email = None
            break
        if validate_email(email):
            break
        print("Invalid email format!")

    # Get additional info
    address = input("Enter address (optional): ").strip() or None
    group = input("Enter group (Friends/Work/Family/Other): ").strip() or "Other"

    contacts[name] = {
        "phone": cleaned_phone,
        "email": email,
        "address": address,
        "group": group,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
    }

    print(f"✅ Contact '{name}' added successfully!")
    return contacts


def search_contacts(contacts: dict, search_term: str):
    """Search contacts by name (partial match)."""
    search_term = search_term.lower()
    results = {}

    for name, info in contacts.items():
        if search_term in name.lower():
            results[name] = info

    return results


def display_search_results(results: dict):
    """Display search results in formatted way."""
    if not results:
        print("No contacts found.")
        return

    print(f"\nFound {len(results)} contact(s):")
    print("-" * 50)

    for i, (name, info) in enumerate(results.items(), 1):
        print(f"{i}. {name}")
        print(f"   📞 Phone: {info['phone']}")
        if info.get("email"):
            print(f"   📧 Email: {info['email']}")
        if info.get("address"):
            print(f"   📍 Address: {info['address']}")
        print(f"   👥 Group: {info.get('group', 'Other')}")
        print()


def display_full_contact(name: str, info: dict):
    print(f"👤 {name}")
    print(f"   📞 {info['phone']}")
    if info.get("email"):
        print(f"   📧 {info['email']}")
    if info.get("address"):
        print(f"   📍 {info['address']}")
    print(f"   👥 {info.get('group', 'Other')}")
    print("----------------------------------------")


def view_all_contacts(contacts: dict):
    """View all contacts."""
    if not contacts:
        print("No contacts available.")
        return

    print(f"\n--- ALL CONTACTS ({len(contacts)} total) ---")
    print("=" * 60)

    for name, info in contacts.items():
        display_full_contact(name, info)


def update_contact(contacts: dict, name: str):
    """Update an existing contact."""
    if name not in contacts:
        print(f"Contact '{name}' not found!")
        return

    print("\n--- UPDATE CONTACT ---")
    print(f"Updating: {name}")

    # Phone
    while True:
        new_phone = input("Enter new phone number (press Enter to keep current): ").strip()
        if not new_phone:
            break
        is_valid, cleaned_phone = validate_phone(new_phone)
        if is_valid:
            contacts[name]["phone"] = cleaned_phone
            break
        print("Invalid phone number! Please enter 10-15 digits.")

    # Email
    while True:
        new_email = input("Enter new email (optional, press Enter to keep current): ").strip()
        if not new_email:
            break
        if validate_email(new_email):
            contacts[name]["email"] = new_email
            break
        print("Invalid email format!")



    # Address
    new_address = input("Enter new address (optional, press Enter to keep current): ").strip()
    if new_address:
        contacts[name]["address"] = new_address

    # Group
    new_group = input("Enter new group (Friends/Work/Family/Other, press Enter to keep current): ").strip()
    if new_group:
        contacts[name]["group"] = new_group

    contacts[name]["updated_at"] = datetime.now().isoformat()
    print(f"✅ Contact '{name}' updated successfully!")


def delete_contact(contacts: dict, name: str):
    """Delete a contact by name."""
    if name not in contacts:
        print(f"Contact '{name}' not found!")
        return

    confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ").lower()
    if confirm == "y":
        del contacts[name]
        print(f"✅ Contact '{name}' deleted successfully!")
    else:
        print("Deletion cancelled.")


def export_to_csv(contacts: dict):
    """Export contacts to CSV."""
    if not contacts:
        print("No contacts to export.")
        return

    fieldnames = ["name", "phone", "email", "address", "group", "created_at", "updated_at"]
    with open(CSV_EXPORT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for name, info in contacts.items():
            row = {"name": name}
            row.update(info)
            writer.writerow(row)

    print(f"✅ Exported contacts to '{CSV_EXPORT_FILE}'.")


def view_statistics(contacts: dict):
    """View statistics about contacts."""
    print("\n--- CONTACT STATISTICS ---")

    total = len(contacts)
    print(f"Total Contacts: {total}")

    # By group
    print("\nContacts by Group:")
    group_counts = {}
    for info in contacts.values():
        group = info.get("group", "Other")
        group_counts[group] = group_counts.get(group, 0) + 1

    if not group_counts:
        print("No group data.")
    else:
        for group, count in sorted(group_counts.items(), key=lambda x: x[0]):
            print(f"  {group}: {count} contact(s)")

    # Recently updated (last 7 days)
    print("\nRecently Updated (last 7 days):", end=" ")
    cutoff = datetime.now() - timedelta(days=7)
    recently_updated = 0
    for info in contacts.values():
        updated_at = info.get("updated_at")
        if not updated_at:
            continue
        try:
            dt = datetime.fromisoformat(updated_at)
            if dt >= cutoff:
                recently_updated += 1
        except ValueError:
            continue

    print(f"{recently_updated}")


def main():
    contacts = load_contacts()

    while True:
        print("\n" + "=" * 26)
        print("          MAIN MENU")
        print("=" * 26)
        print("1. Add New Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("6. Export to CSV")
        print("7. View Statistics")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            contacts = add_contact(contacts)
            save_contacts(contacts)
            print(f"✅ Contacts saved to {DATA_FILE}")

        elif choice == "2":
            search_term = input("Enter name to search: ").strip()
            results = search_contacts(contacts, search_term)
            display_search_results(results)

        elif choice == "3":
            name = input("Enter contact name to update: ").strip()
            update_contact(contacts, name)
            save_contacts(contacts)
            print(f"✅ Contacts saved to {DATA_FILE}")

        elif choice == "4":
            name = input("Enter contact name to delete: ").strip()
            delete_contact(contacts, name)
            save_contacts(contacts)
            print(f"✅ Contacts saved to {DATA_FILE}")

        elif choice == "5":
            view_all_contacts(contacts)

        elif choice == "6":
            export_to_csv(contacts)

        elif choice == "7":
            view_statistics(contacts)

        elif choice == "8":
            save_contacts(contacts)
            print(f"✅ Contacts saved to {DATA_FILE}")
            print("\n" + "=" * 58)
            print("Thank you for using Contact Management System!")
            print("\n" + "=" * 58)
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main() 