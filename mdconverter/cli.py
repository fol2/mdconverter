import click
from pathlib import Path
from .converter import FileConverter

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--output', '-o', type=click.Path(), help='Output file path')
@click.option('--mlm-model', help='MLM model to use for image description')
def main(input_file: str, output: str, mlm_model: str):
    """Convert various file formats to Markdown."""
    try:
        mlm_config = {'model': mlm_model} if mlm_model else None
        converter = FileConverter(mlm_config)
        result = converter.convert_file(input_file)
        
        if output:
            output_path = Path(output)
        else:
            input_path = Path(input_file)
            output_path = input_path.with_suffix('.md')

        output_path.write_text(result)
        click.echo(f"Successfully converted {input_file} to {output_path}")
        
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)
        raise click.Abort()

if __name__ == '__main__':
    main()
